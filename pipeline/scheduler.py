import subprocess
import time

from apscheduler.schedulers.blocking import BlockingScheduler


def run_pipeline():

    print("\nStarting trade intelligence pipeline...\n")

    try:

        # Step 1: Run scraper
        print("Running scraper...")
        subprocess.run(
            ["python", "-m", "scraper.scraper"],
            check=True
        )

        # Step 2: Run cleaner
        print("Running cleaner...")
        subprocess.run(
            ["python", "-m", "cleaning.cleaner"],
            check=True
        )

        # Step 3: Load into PostgreSQL
        print("Loading data into PostgreSQL...")
        subprocess.run(
            ["python", "-m", "pipeline.load_to_db"],
            check=True
        )

        print("\nPipeline completed successfully.\n")

    except subprocess.CalledProcessError as e:

        print(f"\nPipeline failed: {e}\n")


# Create scheduler
scheduler = BlockingScheduler()

# Run every day at 2 AM
scheduler.add_job(
    run_pipeline,
    trigger="cron",
    hour=2,
    minute=0
)


if __name__ == "__main__":

    print("Scheduler started...")
    print("Pipeline scheduled daily at 2:00 AM")

    # Optional immediate test run
    run_pipeline()

    try:

        scheduler.start()

    except (KeyboardInterrupt, SystemExit):

        print("Scheduler stopped.")