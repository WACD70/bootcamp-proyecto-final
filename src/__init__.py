import runpy
def main():
    
    # aquí va todo tu código actual (o encapsulado en funciones)
    runpy.run_module(__name__ + ".data.nyc_taxi_demand_linear_timeseries")
if __name__ == "__main__":
    main()