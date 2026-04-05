import pandas as pd
import numpy as np


def load_clean_data(path: str) -> pd.DataFrame:
    """Carga el dataset limpio desde la ruta indicada."""
    return pd.read_csv(path)


def create_route_column(df: pd.DataFrame) -> pd.DataFrame:
    """Crea la columna route combinando ciudad de origen y destino."""
    df = df.copy()
    df["route"] = df["origin_city"] + " → " + df["destination_city"]
    return df


def add_derived_variables(df: pd.DataFrame) -> pd.DataFrame:
    """Agrega variables derivadas de análisis operacional y económico."""
    df = df.copy()

    df["distance_increase_pct"] = (
        df["extra_distance_km"] / df["original_distance_km"]
    ) * 100

    df["is_disrupted"] = np.where(
        (df["rerouted"] == "Yes") | (df["flight_cancelled"] == "Yes"),
        1,
        0
    )

    df["revenue_per_passenger"] = (
        df["route_revenue_usd"] / df["estimated_passengers"]
    )

    df["fuel_cost_per_passenger"] = (
        df["total_fuel_cost_usd"] / df["estimated_passengers"]
    )

    df["revenue_minus_fuel"] = (
        df["route_revenue_usd"] - df["total_fuel_cost_usd"]
    )

    df["extra_fuel_ratio"] = (
        df["extra_fuel_cost_usd"] / df["total_fuel_cost_usd"]
    )

    return df


def build_phase_summary(df: pd.DataFrame) -> pd.DataFrame:
    """Genera un resumen promedio por fase del conflicto."""
    return df.groupby("conflict_phase").agg({
        "extra_distance_km": "mean",
        "extra_fuel_cost_usd": "mean",
        "total_fuel_cost_usd": "mean",
        "fuel_surcharge_usd": "mean",
        "route_revenue_usd": "mean",
        "estimated_passengers": "mean"
    }).reset_index()


def build_airline_phase_summary(df: pd.DataFrame) -> pd.DataFrame:
    """Genera un resumen por aerolínea y fase."""
    return df.groupby(["airline", "conflict_phase"]).agg({
        "extra_distance_km": "mean",
        "extra_fuel_cost_usd": "mean",
        "route_revenue_usd": "mean",
        "is_disrupted": "mean"
    }).reset_index()


def build_route_phase_summary(df: pd.DataFrame) -> pd.DataFrame:
    """Genera un resumen por ruta y fase."""
    return df.groupby(["route", "conflict_phase"]).agg({
        "extra_distance_km": "mean",
        "extra_fuel_cost_usd": "mean",
        "route_revenue_usd": "mean",
        "distance_increase_pct": "mean"
    }).reset_index()


def build_baseline_route(df: pd.DataFrame) -> pd.DataFrame:
    """Construye el baseline promedio por ruta usando Pre-Pandemic Baseline."""
    baseline = df[df["conflict_phase"] == "Pre-Pandemic Baseline"].groupby("route").agg({
        "total_fuel_cost_usd": "mean",
        "route_revenue_usd": "mean",
        "fuel_surcharge_usd": "mean",
        "extra_distance_km": "mean"
    }).reset_index()

    baseline = baseline.rename(columns={
        "total_fuel_cost_usd": "baseline_fuel_cost",
        "route_revenue_usd": "baseline_revenue",
        "fuel_surcharge_usd": "baseline_surcharge",
        "extra_distance_km": "baseline_extra_distance"
    })

    return baseline


def merge_with_baseline(df: pd.DataFrame, baseline: pd.DataFrame) -> pd.DataFrame:
    """Realiza un merge entre el dataset principal y el baseline por ruta."""
    return df.merge(baseline, on="route", how="left")


def calculate_deltas(df: pd.DataFrame) -> pd.DataFrame:
    """Calcula diferencias respecto al baseline."""
    df = df.copy()

    df["fuel_cost_delta"] = df["total_fuel_cost_usd"] - df["baseline_fuel_cost"]
    df["revenue_delta"] = df["route_revenue_usd"] - df["baseline_revenue"]
    df["surcharge_delta"] = df["fuel_surcharge_usd"] - df["baseline_surcharge"]
    df["extra_distance_delta"] = df["extra_distance_km"] - df["baseline_extra_distance"]

    return df


def build_delta_summary(df: pd.DataFrame) -> pd.DataFrame:
    """Genera un resumen promedio de deltas por fase del conflicto."""
    return df.groupby("conflict_phase").agg({
        "fuel_cost_delta": "mean",
        "revenue_delta": "mean",
        "surcharge_delta": "mean",
        "extra_distance_delta": "mean"
    }).reset_index()


def build_pivots(df: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Construye tablas pivote de costo e ingresos por ruta y fase."""
    pivot_fuel = df.pivot_table(
        values="fuel_cost_delta",
        index="route",
        columns="conflict_phase",
        aggfunc="mean"
    ).reset_index()

    pivot_revenue = df.pivot_table(
        values="revenue_delta",
        index="route",
        columns="conflict_phase",
        aggfunc="mean"
    ).reset_index()

    return pivot_fuel, pivot_revenue