class MetricCalculator:
    """
    简单的指标计算器类，用于计算常见的评估指标。
    
    提供了计算均值、准确率等方法，并支持存储和获取计算结果。
    包含完善的输入验证和边界情况处理。
    """
    
    def __init__(self):
        """初始化计算器，创建空的结果列表。"""
        self.results = []
    
    def calculate_mean(self, data):
        """
        计算数据列表的均值。
        Args:
            data (list): 数值类型的列表
        Returns:
            float: 列表的均值
        Raises:
            TypeError: 当输入不是列表或包含非数值元素时
        """
        # 输入类型验证
        if not isinstance(data, list):
            raise TypeError("数据必须是列表类型")
        
        # 边界情况处理：空列表
        if len(data) == 0:
            return 0.0
        
        # 确保列表中的元素都是数值类型
        try:
            return sum(data) / len(data)
        except TypeError:
            raise TypeError("列表中的所有元素必须是数值类型")
    
    def calculate_accuracy(self, y_true, y_pred):
        """
        计算准确率。
        
        Args:
            y_true (list): 真实标签列表
            y_pred (list): 预测标签列表
            
        Returns:
            float: 准确率值（0.0 到 1.0 之间）
            
        Raises:
            TypeError: 当输入不是列表类型时
        """
        # 输入类型验证
        if not isinstance(y_true, list) or not isinstance(y_pred, list):
            raise TypeError("输入参数必须是列表类型")
        
        # 边界情况处理：空列表或长度不同
        if len(y_true) == 0 or len(y_pred) == 0 or len(y_true) != len(y_pred):
            return 0.0
        
        # 计算正确预测的数量
        correct_count = sum(1 for true, pred in zip(y_true, y_pred) if true == pred)
        return correct_count / len(y_true)
    
    def add_metric(self, name, value):
        """
        添加计算结果到结果列表。
        
        Args:
            name (str): 指标名称
            value (int/float): 指标值
            
        Raises:
            TypeError: 当名称不是字符串或值不是数值时
        """
        # 输入类型验证
        if not isinstance(name, str):
            raise TypeError("指标名称必须是字符串类型")
        
        if not isinstance(value, (int, float)):
            raise TypeError("指标值必须是数值类型")
        
        self.results.append((name, value))
    
    def get_results(self):
        """
        获取所有计算结果。
        
        Returns:
            list: 包含(指标名称, 指标值)元组的列表
        """
        return self.results
