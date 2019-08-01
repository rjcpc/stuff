<?xml version="1.0"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns="http://www.w3.org/TR/xhtml1/strict">
<xsl:template match="/">
<h2>Information</h2>
<xsl:for-each select="students/student">
<br/>
<span style="font-weight:bold;color:teal">
	FirstName : 
</span>
<xsl:value-of select="name/firstname"/>
<br/>
<span style="font-weight:bold;color:teal">
	Lastname :
</span>
<xsl:value-of select="name/lastname"/>
<br/>
<span style="font-weight:bold;color:teal">
	Street :
</span>
<xsl:value-of select="address/street"/>
<br/>
<span style="font-weight:bold;color:teal">
	City :
</span>
<xsl:value-of select="address/city"/>
<br/>
<span style="font-weight:bold;color:teal">
	Email :
</span>
<xsl:value-of select="address/email"/>
<br/>
<span style="font-weight:bold;color:teal">
	Phone :
</span>
<xsl:value-of select="address/phone"/>
<br/>

</xsl:for-each>

</xsl:template>

</xsl:stylesheet>