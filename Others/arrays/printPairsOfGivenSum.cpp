// Input: An array of values and a value k. Print out the pairs whose sum equal val k


#include <iostream>
#include <algorithm>
#include <stdio.h>
// #include <bits/stdc++.h>
using namespace std;

int arr_size = 4;

int partition(int A[],int p,int r){
	int x = A[r];
	int i = p -1;
	int j;
	for (j = p; j <= r-1; j++){
		// cout << " J: "<<A[j]<<" I: "<<A[i] <<endl;
		if(A[j] <= x){
			i++;
			swap(A[i],A[j]);
		}
	}
	swap(A[i+1],A[r]);
	return (i+1);
}

void quicksort(int A[], int p, int r){
	int q;
	if (p < r){
		q = partition(A,p,r);
		quicksort(A,p, q-1);
		quicksort(A,q+1,r);
		// cout << 
	}
}



void getPairsSorting(int array[], int sum){
	quicksort(array, 0, 4);
	

}

int main(){
	int arr[] = {1, 5, 7, -1};
	int k = 6;
	quicksort(arr,0,arr_size-1);
	for (int i =0; i <arr_size;i++){
		cout<<" in: "<<arr[i];
	}
	// getPairsSorting(arr,k)
// arr = [10, 12, 10, 15, -1, 7, 6, 5, 4, 2, 1, 1, 1]
// k = 11
	return 0;

}