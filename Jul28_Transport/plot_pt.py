import numpy as np
import matplotlib.pyplot as plt
import glob
import smash_basic_scripts as sb
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("config_file", help="config file")
args = parser.parse_args()

input_dirs = ["results_wo_rescatt_rr","results_with_rescatt_rr"]
l_styles   = ["--"     ,  "-"]


for i,input_dir in enumerate(input_dirs):
    print(input_dir, i)
    input_files = glob.glob(input_dir+("/*.txt"))
    print (input_files)

    for j, input_file in enumerate(input_files):

        with open(input_file, 'r') as f:
            f.readline()
            pdg = int(f.readline())
            f.readline()
            avg_pt = f.readline()
            f.readline()
            avg_pt_err = f.readline()
            f.readline()
            f.readline()

            bins_and_hist = np.loadtxt(input_file, skiprows=6)
            bin_width = bins_and_hist[0][1] - bins_and_hist[0][0]
            plt.plot(bins_and_hist[0],bins_and_hist[1]/bin_width, label=sb.pdg_to_name(pdg, args.config_file)+" "+input_dir.replace("results_",""), linestyle=l_styles[i])

plt.xlabel(r'$p_T$ [GeV]')
plt.ylabel(r'$dN/dp_T$ [1/GeV]')
plt.legend(ncol=2)
plt.yscale('log')
plt.savefig("pt_spectra.pdf")
plt.cla()


custom_xticks = []
custom_xticks_labels = []
for i,input_dir in enumerate(input_dirs):
    print(input_dir, i)
    input_files = glob.glob(input_dir+("/*.txt"))
    print (input_files)

    for j, input_file in enumerate(input_files):

        with open(input_file, 'r') as f:
            f.readline()
            pdg = int(f.readline())
            f.readline()
            avg_pt = float(f.readline())
            f.readline()
            avg_pt_err = float(f.readline())
            f.readline()
            f.readline()

            print(j, avg_pt, avg_pt_err)

            plt.errorbar(float(j), avg_pt, yerr=avg_pt_err,fmt='o' ,label=sb.pdg_to_name(pdg, args.config_file)+" "+input_dir.replace("results_",""))
            custom_xticks.append(float(j))
            custom_xticks_labels.append(sb.pdg_to_name(pdg, args.config_file))


plt.ylabel(r'$\langle p_T \rangle$ [GeV]')
plt.xticks(ticks=custom_xticks, labels=custom_xticks_labels)
plt.legend()
plt.savefig("pt_avg.pdf")
plt.cla()
