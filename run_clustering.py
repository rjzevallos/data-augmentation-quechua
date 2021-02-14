# coding:utf-8
from source.Cluster import clustering
from source.Cluster import conll_format_clustering
# from source.Cluster.clustering import slot_clustering_and_dump_dict
import argparse
import json


# ============ Args Process ==========
parser = argparse.ArgumentParser()
parser.add_argument("-d", "--data", type=str, default='quchua', help="choose target dataset: quechua")
parser.add_argument("-cm", "--cluster_mode", type=str, default='all', help="select cluster mode: slot, intent, slot-intent, all, no_clustering")
parser.add_argument('--config', default='config_quz.json', help="specific a config file by path")
args = parser.parse_args()

# ============ Settings ==========
with open("config_quz.json", 'r') as con_f:
    CONFIG = json.load(con_f)


def run_clustering():
    if args.data == "quechua":
        print(CONFIG['path']['RawData']['quechua'])
        print(CONFIG['experiment']['train_set_split_rate'])
        conll_format_clustering.clustering_and_dump_dict(
            data_dir=CONFIG['path']['RawData']['quechua'],
            config=CONFIG,
            cluster_mode=args.cluster_mode,
            train_set_split_rate_lst=CONFIG['experiment']['train_set_split_rate'])
    else:
        print("Error: Wrong dataset args.")


if __name__ == "__main__":
    run_clustering()
