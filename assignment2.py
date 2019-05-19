#! /usr/bin/env python3

import vcf
import importlib
import numpy as np

__author__ = 'Lisa Schneider'


class Assignment2:
    
    def __init__(self, main_in_vcf, second_in_vcf):
        self.check_pyvcf_version()

        self.main_name = main_in_vcf
        self.main_reader = vcf.Reader(open(main_in_vcf, "r"))
        self.main_vcf = list(self.main_reader)
        self.second_name = second_in_vcf
        self.second_reader = vcf.Reader(open(second_in_vcf, "r"))

    def check_pyvcf_version(self):
        vcf_exists = importlib.util.find_spec("vcf")
        if vcf_exists:
            if "vcf" in dir():
                print(f"PyVCF version: {vcf.VERSION}")
            else:
                print(f"PyVCF version: {vcf.VERSION}")
        else:
            print("ERROR! pyvcf not installed. "
                  "Run pip3 install pyvcf to install. ")

    def get_average_quality_of_file(self, vcf_reader):
        '''
        Get the average PHRED quality of all variants
        :return:
        '''
        quality_list = []
        for record in vcf_reader:
            quality_list.append(record.QUAL)
        phred_quality = np.mean(quality_list)
        print(f"Average PHRED quality: {phred_quality}")

        # quality_list = []
        # for record in vcf_reader:
        #     quality_list.append(record.samples[0]["GQ"])
        # phred_quality = np.mean(quality_list)
        # phred_quality = np.round(phred_quality, decimals=2)
        # print(f"Average PHRED quality: {phred_quality}")

    def get_total_number_of_variants_of_file(self, vcf_reader):
        '''
        Get the total number of variants
        :return: total number of variants
        '''
        variant_counter = 0
        for variant_counter in range(len(vcf_reader)):
            variant_counter += 1
        print(f"Total number of variants: {variant_counter}")
    
    def get_variant_caller_of_vcf(self, vcf_reader):
        '''
        Return the variant caller name
        :return: 
        '''
        caller_list = []
        for record in vcf_reader:
            callers = record.INFO["callsetnames"]
            for i in range(len(callers)):
                caller_list.append(callers[i])
        print(f"Variant callers: {set(caller_list)}")
        

    def get_human_reference_version(self, vcf_reader):
        '''
        Return the genome reference version
        :return: 
        '''
        for record in vcf_reader:
            try:
                info = record.INFO['difficultregion'][0][0:4]
            except:
                info = None
            if info is not None:
                reference = info
        print(f"Human reference version: {reference}")


    def get_number_of_indels(self, vcf_reader):
        '''
        Return the number of identified INDELs
        :return:
        '''
        indel_counter = 0
        for record in vcf_reader:
            if record.is_indel:
                indel_counter += 1
        print(f"Number of indels: {indel_counter}")

    def get_number_of_snvs(self, vcf_reader):
        '''
        Return the number of SNVs
        :return: 
        '''
        snp_counter = 0
        for record in vcf_reader:
            if record.is_snp:
                snp_counter += 1
        print(f"Number of SNVs: {snp_counter}")

        
    def get_number_of_heterozygous_variants(self, vcf_reader):
        '''
        Return the number of heterozygous variants
        :return: 
        '''
        # hetero_counter1 = 0
        # for record in vcf_reader:
        #     if record.samples[0]["GT"] == "0|1" or ["GT"] == "1|0":
        #         hetero_counter1 += 1
        # print(f"Number of heterozygous variants: {hetero_counter1}")

        hetero_counter = 0
        for record in vcf_reader:
            hetero_counter += record.num_het
        print(f"Number of heterozygous variants: {hetero_counter}")

    
    def merge_chrs_into_one_vcf(self, main_file, second_file):
        '''
        Creates one VCF containing all variants of chr21 and chr22
        :return:
        '''
        main_reader = vcf.Reader(open(main_file))
        main_writer = vcf.Writer(open("merged.vcf", "w+"), main_reader)
        line_count = 0
        for record in main_reader:
            main_writer.write_record(record)
            line_count += 1

        second_reader = vcf.Reader(open(second_file))
        second_writer = vcf.Writer(open("merged.vcf", "a"), second_reader)
        for record in second_reader:
            second_writer.write_record(record)
            line_count += 1

        print(f"Number of lines in merged file: {line_count}")
        
    
    def print_summary(self):
        self.get_average_quality_of_file(self.main_vcf)
        self.get_total_number_of_variants_of_file(self.main_vcf)
        self.get_variant_caller_of_vcf(self.main_vcf)
        self.get_human_reference_version(self.main_vcf)
        self.get_number_of_indels(self.main_vcf)
        self.get_number_of_snvs(self.main_vcf)
        self.get_number_of_heterozygous_variants(self.main_vcf)  
        self.merge_chrs_into_one_vcf(self.main_name, self.second_name)
    
    
def main():
    print("Assignment 2")
    assignment2 = Assignment2("chr22_new.vcf", "chr21_new.vcf")
    assignment2.print_summary()
    print("Done with assignment 2")

        
if __name__ == '__main__':
    main()
   
    



