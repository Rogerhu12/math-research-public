# 固定三挠曲线 Cartier 比较的符号核验契约

2026-11-20，serre-public-astra-20261120-de0a3e3b。**待公开 Actions 回执；不预填恒等式核验成功。**

新候选固定曲线为
$$
E_T:Y^2=f(X,T)=X^3+(12T-15)X+4T^2-28T+22.
$$
拟议的原三分位 Cartier 比较使用三个可有限精确核验的证书：Legendre 微分方程的全 $X$ 导数证书、$dX/(2Y)$ 的 Gauss–Manin 精确项，以及核由 $(3,2(T+1))$ 生成的规范三同源。它们的全部多项式、每个有理分母和原 $s^2=-3$ 缩放都完整写在 `scripts/p11_fixed_cartier_symbolic.py` 中。

脚本在标准库 `Fraction` 的稀疏 $\mathbf Q[T,X,Y]$ 中清分母后逐系数相减；结果必须为零多项式。它同时核对 $f_{TT}=8$、判别式、Tate 三挠换元、同源导数分子，以及 $\mathbf Q(s)$ 中坐标和微分的九项缩放身份。全系数有理恒等式足以核实这些代数证书，不用有限素数样本替代。若失败，保留精确非零残差摘要并非零退出。

这里不重算 run `44718206366` 的 203 个素数窗口，不重证旧 `543d03f8` 已完成的本原三分位双标签及 Legendre 不共零结论，不假定固定曲线普通或 CM，也不推断指定 σ 乘积单位。完整原来源论证须另行审核后登记。

执行：`scripts/p11_fixed_cartier_symbolic.py --output /tmp/p11-fixed-cartier-symbolic.json`。只允许本公开仓库 Actions；临时输出不入 Git 或 Release，本地只读源、AST 与哈希。
