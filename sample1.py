class sample1:
	def __init__(self, asset_display_ipv4_address, asset_name, asset_operating_system, asset_system_type, asset_tags, definition_cpe, definition_cve, 
	      definition_cvss3_base_score, definition_family, definition_id, definition_name, definition_patch_published, definition_plugin_published, 
		  definition_vpr_drivers_product_coverage, definition_vpr_score, definition_vulnerability_published, first_observed, id, last_seen, output, 
		  port, scan_id, severity, state):
		self.asset_display_ipv4_address = asset_display_ipv4_address
		self.asset_name = asset_name
		self.asset_operating_system = asset_operating_system
		self.asset_system_type = asset_system_type
		self.asset_tags = asset_tags
		self.definition_cpe = definition_cpe
		self.definition_cve = definition_cve
		self.definition_cvss3_base_score = definition_cvss3_base_score
		self.definition_family = definition_family
		self.definition_id = definition_id
		self.definition_name = definition_name
		self.definition_patch_published = definition_patch_published
		self.definition_plugin_published = definition_plugin_published
		self.definition_vpr_drivers_product_coverage = definition_vpr_drivers_product_coverage
		self.definition_vpr_score = definition_vpr_score
		self.definition_vulnerability_published = definition_vulnerability_published
		self.first_observed = first_observed
		self.id = id
		self.last_seen = last_seen
		self.output = output
		self.port = port
		self.scan_id = scan_id
		self.severity = severity
		self.state = state

	def getAsset_display_ipv4_address(self):
		return self.asset_display_ipv4_address

	def getAsset_name(self):
		return self.asset_name

	def getAsset_operating_system(self):
		return self.asset_operating_system

	def getAsset_system_type(self):
		return self.asset_system_type

	def getAsset_tags(self):
		return self.asset_tags

	def getDefinition_cpe(self):
		return self.definition_cpe

	def getDefinition_cve(self):
		return self.definition_cve

	def getDefinition_cvss3_base_score(self):
		return self.definition_cvss3_base_score

	def getDefinition_family(self):
		return self.definition_family

	def getDefinition_id(self):
		return self.definition_id

	def getDefinition_name(self):
		return self.definition_name

	def getDefinition_patch_published(self):
		return self.definition_patch_published

	def getDefinition_plugin_published(self):
		return self.definition_plugin_published

	def getDefinition_vpr_drivers_product_coverage(self):
		return self.definition_vpr_drivers_product_coverage

	def getDefinition_vpr_score(self):
		return self.definition_vpr_score

	def getDefinition_vulnerability_published(self):
		return self.definition_vulnerability_published

	def getFirst_observed(self):
		return self.first_observed

	def getId(self):
		return self.id

	def getLast_seen(self):
		return self.last_seen

	def getOutput(self):
		return self.output

	def getPort(self):
		return self.port

	def getScan_id(self):
		return self.scan_id

	def getSeverity(self):
		return self.severity

	def getState(self):
		return self.state

	def setAsset_display_ipv4_address(self, asset_display_ipv4_address):
		self.asset_display_ipv4_address = asset_display_ipv4_address

	def setAsset_name(self, asset_name):
		self.asset_name = asset_name

	def setAsset_operating_system(self, asset_operating_system):
		self.asset_operating_system = asset_operating_system

	def setAsset_system_type(self, asset_system_type):
		self.asset_system_type = asset_system_type

	def setAsset_tags(self, asset_tags):
		self.asset_tags = asset_tags

	def setDefinition_cpe(self, definition_cpe):
		self.definition_cpe = definition_cpe

	def setDefinition_cve(self, definition_cve):
		self.definition_cve = definition_cve

	def setDefinition_cvss3_base_score(self, definition_cvss3_base_score):
		self.definition_cvss3_base_score = definition_cvss3_base_score

	def setDefinition_family(self, definition_family):
		self.definition_family = definition_family

	def setDefinition_id(self, definition_id):
		self.definition_id = definition_id

	def setDefinition_name(self, definition_name):
		self.definition_name = definition_name

	def setDefinition_patch_published(self, definition_patch_published):
		self.definition_patch_published = definition_patch_published

	def setDefinition_plugin_published(self, definition_plugin_published):
		self.definition_plugin_published = definition_plugin_published

	def setDefinition_vpr_drivers_product_coverage(self, definition_vpr_drivers_product_coverage):
		self.definition_vpr_drivers_product_coverage = definition_vpr_drivers_product_coverage

	def setDefinition_vpr_score(self, definition_vpr_score):
		self.definition_vpr_score = definition_vpr_score

	def setDefinition_vulnerability_published(self, definition_vulnerability_published):
		self.definition_vulnerability_published = definition_vulnerability_published

	def setFirst_observed(self, first_observed):
		self.first_observed = first_observed

	def setId(self, id):
		self.id = id

	def setLast_seen(self, last_seen):
		self.last_seen = last_seen

	def setOutput(self, output):
		self.output = output

	def setPort(self, port):
		self.port = port

	def setScan_id(self, scan_id):
		self.scan_id = scan_id

	def setSeverity(self, severity):
		self.severity = severity

	def setState(self, state):
		self.state = state
