class Step2Utilities(object):
    
    def __init__(self, parent=None):
        self.parent = parent
        
    def is_table_empty(self):
        if not self.parent.ui.table.rowCount() > 0:
            return True
        else:
            return False
        
    def at_least_one_row_checked(self):
        o_table_handler = TableHandler(parent = self.parent)
        o_table_handler.retrieve_list_of_selected_rows()
        list_of_selected_row = o_table_handler.list_selected_row
        if len(list_of_selected_row) > 0:
            return True
        else:
            return False
        
    def is_fourier_filter_from_empty(self):
        _from = str(self.parent.ui.fourier_filter_from.text()).strip()
        if _from == "":
            return True
        else:
            return False
        
    def is_fourier_filter_to_empty(self):
        _to = str(self.parent.ui.fourier_filter_to.text()).strip()
        if _to == "":
            return True
        else:
            return False
        
    def any_fourier_filter_widgets_empty(self):
        _from = str(self.parent.ui.fourier_filter_from.text()).strip()
        if _from == "":
            return True
        
        _to = str(self.parent.ui.fourier_filter_to.text()).strip()
        if _to == "":
            return True
        
        return False
        
    def any_plazcek_widgets_empty(self):
        _min = str(self.parent.ui.plazcek_fit_range_min.text()).strip()
        if _min == "":
            return True
    
        _max = str(self.parent.ui.plazcek_fit_range_max.text()).strip()
        if _max == "":
            return True

        return False
        
    def any_q_range_widgets_empty(self):
        _min = str(self.parent.ui.q_range_min.text()).strip()
        if _min == "":
            return True
    
        _max = str(self.parent.ui.q_range_max.text()).strip()
        if _max == "":
            return True

        return False
        

class TableHandler(object):
    
    def __init__(self, parent=None):
        self.parent=parent
                
    def retrieve_list_of_selected_rows(self):
        self.list_selected_row = []
        for _row_index in range(self.parent.ui.table.rowCount()):
            _widgets = self.parent.ui.table.cellWidget(_row_index, 0).children()
            if len(_widgets) > 0:
                _selected_widget = self.parent.ui.table.cellWidget(_row_index, 0).children()[1]
                if (_selected_widget.checkState() == Qt.Checked):
                    _entry = self._collect_metadata(row_index = _row_index)
                    self.list_selected_row.append(_entry)

    def _collect_metadata(self, row_index = -1):
        if row_index == -1:
            return []
        
        _name = self.retrieve_item_text(row_index, 1)
        _runs = self.retrieve_item_text(row_index, 2)
        _sample_formula = self.retrieve_item_text(row_index, 3)
        _mass_density = self.retrieve_item_text(row_index, 4)
        _radius = self.retrieve_item_text(row_index, 5)
        _packing_fraction = self.retrieve_item_text(row_index, 6)
        _sample_shape = self._retrieve_sample_shape(row_index)
        _do_abs_correction = self._retrieve_do_abs_correction(row_index)
        
        _metadata = {'name': _name,
                     'runs': _runs,
                     'sample_formula': _sample_formula,
                     'mass_density': _mass_density,
                     'radius': _radius,
                     'packing_fraction': _packing_fraction,
                     'sample_shape': _sample_shape,
                     'do_abs_correction': _do_abs_correction}
        
        return _metadata

    def retrieve_item_text(self, row, column):
        _item = self.parent.ui.table.item(row, column)
        if _item is None:
            return ''
        else:
            return str(_item.text())
        
    def _retrieve_sample_shape(self, row_index):
        _widget = self.parent.ui.table.cellWidget(row_index, 7)
        _selected_index = _widget.currentIndex()
        _sample_shape = _widget.itemText(_selected_index)
        return _sample_shape
            
    def _retrieve_do_abs_correction(self, row_index):
        _widget = self.parent.ui.table.cellWidget(row_index, 8).children()[1]
        if (_widget.checkState() == Qt.Checked):
            return 'go'
        else:
            return 'nogo'