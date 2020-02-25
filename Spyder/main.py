from ScrapQueue.queue import ScrapQueue

scrapQueue = ScrapQueue()

urls = ['https://facebook.com/', 'https://google.com/', 'https://imdeepmind.com/']

scrapQueue.add_jobs(urls)

scrapQueue.run_batch()

print(scrapQueue.jobs)