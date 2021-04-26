import tabula

from tabula import read_pdf    
# df = read_pdf("WB/Vacant_bed_status_as_on_26.04_.21_.pdf")


tabula.convert_into("WB/Vacant_bed_status_as_on_26.04_.21_.pdf", "WB/Vacant_bed_status_as_on_26.04_.21_.csv", output_format="csv", pages='all')


# df = tabula.read_pdf("WB/Vacant_bed_status_as_on_26.04_.21_.pdf", encoding='utf-8', lattice=True, pages='1')
# print(df)


# df.to_csv('Vacant_bed_status_as_on_26.04_.21_.csv', encoding='utf-8')
# print(df[0])

