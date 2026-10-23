#!/usr/bin/env python3
import sys
from datetime import date
from dateutil.relativedelta import relativedelta
from ruamel.yaml import YAML

CONFIG = "/scratch/b56h/rayne.b56h/GCClassic/run_dirs/JPL20_kin_only/geoschem_config.yml"
CHUNK_MONTHS = 4
FINAL_END = date(2021, 1, 1)  # overall simulation target end date

yaml = YAML()
yaml.preserve_quotes = True
yaml.width = 4096  # avoid line-wrapping long lines

with open(CONFIG) as f:
    cfg = yaml.load(f)

start_ymd, start_hms = cfg["simulation"]["start_date"]
end_ymd, end_hms = cfg["simulation"]["end_date"]

end_date = date(end_ymd // 10000, (end_ymd // 100) % 100, end_ymd % 100)

if end_date >= FINAL_END:
    print("FINISHED")
    sys.exit(0)

new_start_date = end_date
new_end_date = min(new_start_date + relativedelta(months=CHUNK_MONTHS), FINAL_END)

cfg["simulation"]["start_date"][0] = int(new_start_date.strftime("%Y%m%d"))
cfg["simulation"]["end_date"][0] = int(new_end_date.strftime("%Y%m%d"))


with open(CONFIG, "w") as f:
    yaml.dump(cfg, f)

print(f"Advanced to {new_start_date} -> {new_end_date}")