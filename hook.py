def zap_pre_shutdown(zap):
	print("Hook Identified")
	print(zap.stats.site_stats("http://testphp.vulnweb.com/", "stats.auth"))
