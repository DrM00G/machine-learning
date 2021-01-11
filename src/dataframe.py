class DataFrame:
    def __init__(self,data_dict,column_order=None):
        self.columns = column_order
        self.ordered_dict = {}
        if column_order==None:
          self.columns = [unit for unit in data_dict]
          self.ordered_dict = data_dict
        else:
          for colomn in self.columns:
            self.ordered_dict[colomn] = data_dict[colomn]
        
    def to_array(self):
        result = [[] for colomn in self.ordered_dict[self.columns[0]]]
        for result_col in range(len(self.ordered_dict[self.columns[0]])):
            for col_name in self.columns:
                result[result_col].append(self.ordered_dict[col_name][result_col])

        return result

    def filter_columns(self,filter_cols):
        return DataFrame(self.ordered_dict, filter_cols)
    
    def apply(self, column, f):
      for value in range(len(self.ordered_dict[column])):
        self.ordered_dict[column][value] = f(self.ordered_dict[column][value])
      return DataFrame(self.ordered_dict, self.columns)

    def append_pairwise_interactions(self):
      amalgams = []
      for column in range(len(self.columns)):
        for column2 in range(len(self.columns)):
          if column2 > column:
            amalgams.append([self.columns[column],self.columns[column2],[]])
            for value in range(len(self.ordered_dict[self.columns[column]])):
              amalgams[len(amalgams)-1][2].append(self.ordered_dict[self.columns[column]][value] * self.ordered_dict[self.columns[column2]][value])
      modified_columns = []
      modified_dict = {}
      for colomn in self.columns:
          modified_columns.append(colomn)
          modified_dict[colomn] = self.ordered_dict[colomn]
      for column in amalgams:
        modified_columns.append(column[0]+"_"+column[1])
        modified_dict[column[0]+"_"+column[1]] = column[2]
      return DataFrame(modified_dict, modified_columns)

    def create_dummy_variables(self):
        new_dict = self.ordered_dict
        data_columns = []
        for key in new_dict:
            if isinstance(new_dict[key][0],str) or isinstance(new_dict[key][0],list):
                data_columns.append(key)
        for key in data_columns:
            if isinstance(new_dict[key][0], str):
                for dummy in self.data_dict[key]:
                    new_dict.update({(key + "_" + dummy):[1 if dummy == data else 0 for data in self.data_dict[key]]})
            elif isinstance(new_dict[key][0], list):
                dumb_vars = []
                for arr in new_dict[key]:
                  for var in arr:
                    if var not in dumb_vars:
                      dumb_vars.append(var)
                transformed_data = self.modify_list_data(dumb_vars, new_dict[key])
                for i in range(len(dumb_vars)):
                    new_dict.update({dumb_vars[i]:transformed_data[i]})
            del new_dict[key]
        return DataFrame(new_dict)

    def modify_list_data(self, dum_vars, data):
        new_data = [[] for i in range(len(dum_vars))]
        for arr in data:
            for dummy in dum_vars:
                ind_of_dummy = dum_vars.index(dummy)
                if dummy in arr:
                    new_data[ind_of_dummy].append(1)
                else:
                    new_data[ind_of_dummy].append(0)
        return new_data

    def swap_columns(self, column1_indx, column2_indx):
        new_columns = [column for column in self.columns]
        new_columns[column1_indx] = self.columns[column2_indx]
        new_columns[column2_indx] = self.columns[column1_indx]
        return DataFrame(self.ordered_dict, new_columns)

    def append_columns(self, new_columns, column_order = None):
        result = self.ordered_dict
        for column in new_columns:
            result[column] = new_columns[column]
        return DataFrame(result)

    def remove_columns(self,columns):
        result = {}
        for column in self.ordered_dict:
            if column not in columns:
                result[column] = self.ordered_dict[column]
        return DataFrame(result)


    @classmethod
    def from_array(cls, arr, columns):
        data_dict = {}
        for i in range(len(columns)):
            data_dict[columns[i]] = []
            for n in range(len(arr)):
                data_dict[columns[i]].append(arr[n][i])
        result = cls(data_dict)
        return result
      

    def select_columns(self, columns):
        return DataFrame({column:self.ordered_dict[column] for column in columns})


    def select_rows(self, index_list):
        return DataFrame.from_array([self.to_array()[n] for n in index_list], self.columns)

    def select_rows_where(self, lamda):
        arr = self.to_array()
        result = []
        for row in arr:
            lamda_row = {self.columns[i]:row[i] for i in range(len(row))}
            if lamda(lamda_row):
                result.append(row)
        return DataFrame.from_array(result, self.columns)

    def order_by(self, column, ascending):
      if ascending:
        if isinstance(self.ordered_dict[column][0],str):
          alphabet = [ord(word[0]) for word in self.ordered_dict[column]]
          order = self.sort(alphabet)
          return DataFrame.from_array([self.to_array()[i] for i in order], self.columns)
        else:
          order = self.sort(self.ordered_dict[column])
          return DataFrame.from_array([self.to_array()[i] for i in order], self.columns)

      else:
        if isinstance(self.ordered_dict[column][0],str):
          alphabet = [ord(word[0]) for word in self.ordered_dict[column]]
          order = self.sort(alphabet)[::-1]
          return DataFrame.from_array([self.to_array()[i] for i in order], self.columns)
        else:
          order = self.sort(self.ordered_dict[column])[::-1]
          return DataFrame.from_array([self.to_array()[i] for i in order], self.columns)

    def sort(self, arr):
        data_arr = [entry for entry in arr]
        index = [i for i in range(len(data_arr))]
        for i in range(len(data_arr)):
            for n in range(len(data_arr)-(i+1)):
                if data_arr[n] > data_arr[n+1]:
                    temp=[data_arr[n],index[n]]
                    data_arr[n]= data_arr[n + 1]#just to switch
                    data_arr[n + 1]= temp[0]
                    index[n]= index[n + 1]  
                    index[n + 1]= temp[1]
        return index