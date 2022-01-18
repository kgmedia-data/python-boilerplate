import argparse
import scripts

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument('--params', required=False)

    params = parser.parse_args()

    job = scripts.job.Job(params)
    job.run()
