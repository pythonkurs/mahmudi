import urllib2
import untangle

def getting_datai():
    file = urllib2.urlopen('http://www.grandcentral.org/developers/data/nyct/nyct_ene.xml')
    data = file.read()
#close file because we dont need it anymore:
    file.close()
    #parse the xml downloaded
    doc = untangle.parse(data)

    #retrieve the first xml tag (<tag>data</tag>) that the parser finds with name tagName:
    outages = doc.NYCOutages.outage

    total_outages= len(outages)
    repair_count=0
    for i in range(total_outages):
        outage = outages[i]
        if outage.reason.cdata == "REPAIR":
            repair_count=repair_count+1

    fraction = repair_count/float(total_outages)
    print "Fraction of outages having the reason REPAIR is " + str(fraction)
