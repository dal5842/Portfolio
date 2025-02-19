<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:xs="http://www.w3.org/2001/XMLSchema"
    xmlns:math="http://www.w3.org/2005/xpath-functions/math"
    xmlns:xd="http://www.oxygenxml.com/ns/doc/xsl"
    exclude-result-prefixes="xs math xd"
    version="3.0">
    <xsl:output method="xml" indent="yes"/>
    
    <!-- Match root element -->
    <xsl:template match="/novel">
        <novel>
            <xsl:apply-templates/>
        </novel>
    </xsl:template>
    
    <!-- Process paragraphs -->
    <xsl:template match="p">
        <p>
            <xsl:apply-templates/>
        </p>
    </xsl:template>
    
    <!-- Process journal entries -->
    <xsl:template match="journal">
        <journal author="{@author}">
            <xsl:apply-templates/>
        </journal>
    </xsl:template>
    
    <!-- Process letters -->
    <xsl:template match="letter">
        <letter from="{@from}" to="{@to}">
            <xsl:apply-templates/>
        </letter>
    </xsl:template>
    
    <!-- Quotes -->
    <xsl:template match="text()">
        <xsl:analyze-string select="." regex='"([^"]+)"'>
            <xsl:matching-substring>
                <quote>
                    <xsl:value-of select="regex-group(1)"/>
                </quote>
            </xsl:matching-substring>
            <xsl:non-matching-substring>
                <xsl:value-of select="."/>
            </xsl:non-matching-substring>
        </xsl:analyze-string>
    </xsl:template>
    
    <!-- Dates -->
    <xsl:template match="text()" mode="tag_dates">
        <xsl:analyze-string select="." regex="\b(\d{{1,2}} [A-Za-z]+)\b">
            <xsl:matching-substring>
                <date><xsl:value-of select="."/></date>
            </xsl:matching-substring>
            <xsl:non-matching-substring>
                <xsl:value-of select="."/>
            </xsl:non-matching-substring>
        </xsl:analyze-string>
    </xsl:template>
</xsl:stylesheet>