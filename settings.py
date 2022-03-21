BOT_NAME = 'myra'

SPIDER_MODULES = ['myra.spiders']
NEWSPIDER_MODULE = 'myra.spiders'
ITEM_PIPELINES = {'myra.pipelines.myra': 100}