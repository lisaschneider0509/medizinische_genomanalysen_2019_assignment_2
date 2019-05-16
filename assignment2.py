#! /usr/bin/env python3

import vcf
import importlib
import numpy as np

__author__ = 'XXX'


class Assignment2:
    
    def __init__(self, main_vcf, second_vcf):
        self.main_vcf = self.read_vcf(main_vcf)
        self.second_vcf = self.read_vcf(second_vcf)


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

    def read_vcf(self, vcf_name):
        vcf_reader = vcf.Reader(open(vcf_name, "r"))
        record_list = []
        for record in vcf_reader:
            record_list.append(record)
        return record_list

    def get_average_quality_of_file(self, record_list):
        '''
        Get the average PHRED quality of all variants
        :return:
        '''
        quality_list = []
        for record in record_list:
            quality_list.append(record.samples[0]["GQ"])
        phred_quality = np.mean(quality_list)
        phred_quality = np.round(phred_quality, decimals=2)
        print(f"Average PHRED quality: {phred_quality}")
        return phred_quality

        
    def get_total_number_of_variants_of_file(self, record_list):
        '''
        Get the total number of variants
        :return: total number of variants
        '''
        print("Calculating total_number_of_variants. This may take a while...")
        variant_counter = 0
        for record in record_list:
            variant_counter += 1
        print(f"Total number of variants: {variant_counter}")
    
    def get_variant_caller_of_vcf(self, record_list):
        '''
        Return the variant caller name
        :return: 
        '''
        for record in record_list:
            print(record)
        print(f"Variant caller of vcf: TODO")
        
        
    def get_human_reference_version(self):
        '''
        Return the genome reference version
        :return: 
        '''
        print("TODO")
        
        
    def get_number_of_indels(self, record_list):
        '''
        Return the number of identified INDELs
        :return:
        '''
        indel_counter = 0
        for record in record_list:
            if record.is_indel:
                indel_counter += 1
        print(f"Number of indels: {indel_counter}")

    def get_number_of_snvs(self, record_list):
        '''
        Return the number of SNVs
        :return: 
        '''
        snp_counter = 0
        for record in record_list:
            if record.is_snp:
                snp_counter += 1
        print(f"Number of SNVs: {snp_counter}")
        
    def get_number_of_heterozygous_variants(self, record_list):
        '''
        Return the number of heterozygous variants
        :return: 
        '''
        hetero_counter = 0
        for record in record_list:
            if record.samples[0]["GT"] == "0|1" or ["GT"] == "1|0":
                hetero_counter += 1
        print(f"Number of heterozygous variants: {hetero_counter}")

        
    
    def merge_chrs_into_one_vcf(self, main_vcf, second_vcf):
        '''
        Creates one VCF containing all variants of chr21 and chr22
        :return:
        '''
        print("Number of total variants")
        
    
    def print_summary(self):
        # self.check_pyvcf_version()
        # self.get_average_quality_of_file(self.main_vcf, "chr22.vcf")
        # self.get_total_number_of_variants_of_file(self.main_vcf[0:5])
        self.get_variant_caller_of_vcf(self.main_vcf)
        # self.get_number_of_indels(self.main_vcf)
        # self.get_number_of_snvs(self.main_vcf)
        # self.get_number_of_heterozygous_variants(self.main_vcf)
        # self.merge_chrs_into_one_vcf("chr22.vcf", "chr22.vcf")
    
    
def main():
    print("Assignment 2")
    assignment2 = Assignment2("chr22.vcf", "chr22.vcf")
    assignment2.print_summary()
    print("Done with assignment 2")
        
        
if __name__ == '__main__':
    main()
   
    



