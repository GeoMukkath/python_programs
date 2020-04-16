def insertion_sort(l):
	i = 0 ;
	while i < len(l):
			if l[i] > l[i +1]:
				l[i], l[i+1] = l[i +1], l[i];
				i = i +1;
			else:
				i = i + 1 ;
	
	return lst; 

lst = [34,12,56,4,90,66];

insertion_sort(lst);