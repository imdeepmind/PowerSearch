from Scraper.scraper import Scrapper

from logger.logger import logger

JOB_SCHEDULED = 'JOB_SCHEDULED'
JOB_RUNNING = 'JOB_RUNNING'
JOB_DONE = 'JOB_DONE'
JOB_FAILED = 'JOB_FAILED'

print(logger.error)

class ScrapQueue:
  def __init__(self, nJobs=4):
    super().__init__()
    self.jobs = []
    self.nJobs = nJobs

  def __generate_job_id(self):
    return len(self.jobs)
  
  def __find_by_id(self, id):
    return self.jobs[id]
  
  def __add_job_result(self, id, result):
    self.jobs[id]['result'] = result
  
  def __add_job_error(self, id, error):
    self.jobs[id]['error'] = error
  
  def __run_scrape(self, id):
    try:
      logger.info('Running scraper')
      job = self.__find_by_id(id)
      scraper = Scrapper(3)
      result = scraper.scrap(job['url'])
      self.__add_job_result(id, result)
    except ValueError as ve:
      logger.exception(ve)
      self.__add_job_error(id, ve)
    except Exception as ex:
      logger.exception(ve)
      self.__add_job_error(id, ex)

  def __no_job_to_start(self):
    running = 0
    
    for job in self.jobs:
      if job['status'] == JOB_RUNNING:
        running += 1

    return self.nJobs - running

  def __no_jobs_available(self):
    nJobsAvailable = 0

    for job in self.jobs:
      if job['status'] == JOB_SCHEDULED:
        nJobsAvailable += 1

    return nJobsAvailable
  
  def __get_available_job(self):
    for index, job in enumerate(self.jobs):
      if job['status'] == JOB_SCHEDULED:
        return index

  def add_jobs(self, jobs):
    logger.info('Adding new jobs')
    for job in jobs:
      self.jobs.append({
        'url' : job,
        'status': JOB_SCHEDULED,
        'result': None,
        'error': None
      })

  def run_batch(self):
    logger.info('Running a new batch')
    availableThreads = self.__no_job_to_start()
    availableJobs = self.__no_jobs_available()

    n = min(availableJobs, availableThreads)

    for _ in range(n):
      id = self.__get_available_job()
      self.__run_scrape(id)