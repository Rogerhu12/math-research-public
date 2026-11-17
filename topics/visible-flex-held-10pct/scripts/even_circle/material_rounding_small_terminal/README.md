# q05小步圆化的最后两条实际结果

初始λ=.0001记录在material_rounding_initial；本包补全同一次实际循环的λ=.0003/.001结果，两条都solver接受但完整metric失败。实际args、源hash、物理参数、检查点hash全部在completed.json。源码复用material_restart，后两步沿用上一步solver系数初值，没有另声称材料角回拉恒等核验。全部原门保持，未得到圆弧或闭族。
