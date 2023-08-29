from benchmark import benchmarker


def main():
    functions_to_run = [
        "difference_collection",
    ]

    # Uncomment to run everything
    # functions_to_run = None
    benchmarker.run_benchmarks(
        modules_to_run=["benchmarks_shapely"],
        functions_to_run=functions_to_run,
    )


if __name__ == "__main__":
    main()
