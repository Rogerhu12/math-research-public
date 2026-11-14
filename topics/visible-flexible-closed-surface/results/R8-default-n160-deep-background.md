# R8：默认 N160 未改深背景的严格曲率与 C² 平帽

会话：Astra-visible-flex-4ffd372b / closing_geometry。2026-11-09。
状态：完整背景证明，独审PASS（notes/2026-11-09-audit-deep-background-n160.md）；不含有限warp积分认证，也不含非轴对称等距扰动。

## 已核输入

邻题 `large-amplitude-twist-flex/results/R28-fixed-deep-background-c2-cuff.md` §1
Git blob `cf9881e3ae2c2797a61213ab099dbec239be5f0d`。
本地旧cache字节已核同此blob，全文已读。它证明默认
$$R=64,\quad a=11/4,\quad \delta_n=.006\,2^{-n},\quad c_n=.05\,2^{-n/2}$$
的每个n≥80有exact校准根alpha_n∈[.5,2]。
这里只选定一个固定括号根，不需唯一性。R28的旧rCuff数值常数没有移植。

本题当前N160候选固定r_c=1/4、w_cut=1/2、delta0=3/500。
所有浅层valley/pulse/flat-sleeve探索只改有限保护部分；从n≥160开始均是下述同一深源。

## 全深度估计

记原始总对数长度Y、归一化epsilon为
$$Y=6\delta_0+\frac{6(.05\delta_0)}{1-2^{-3/2}},\qquad
\epsilon=\frac{w_{cut}(r_c e^{Y/\sqrt{12}})^7}{(2\delta_0)^{11/4}}.$$
括号根使各cell平台p≤64，最大log跳跃≤H_n=log(128/delta_n²)。因此
$$0<w\le W_n:=\frac{\epsilon64\delta_n^{7/4}}{r_c^7},$$
$$|w_r|\le B_n:=\frac{\sqrt{12}W_n(15/8)H_n}{r_c\eta_n}+\frac{7W_n}{r_c},
\qquad\eta_n=.05\delta_0\,2^{-3n/2}.$$
这使用max S'=15/8的保守界；不需要采样找到转折最大值。

有严格的简单常数：2^(-3/2)<3/8，Y<.03888，sqrt(12)>3，2^(11/4)>6，
且exp(7Y/sqrt(12))<10/9。因此
$$W_{160}<\frac{80000}{81}\,2^{-280}.$$
由log2<.7和log(500/3)<6，H_160<241。代入sqrt(12)<7/2，
$$B_{160}<\frac72\frac{80000}{81}2^{-280}\frac{15}{8}
\frac{241}{(1/4)(3/10000)2^{-240}}+28\frac{80000}{81}2^{-280}<\frac1{50}.$$
全部常数用附带Python的Fraction和整数比较复算。

第一项的粗上包络是常数乘2^(-n/4)(1.4n+16.9)。n≥160时每步比值
小于((H+1.4)/H)(6/7)<1，因为2^(1/4)>7/6。
第二项按2^(-7n/4)下降。故**所有**未改n≥160的母线曲率都小于.02，
圆周曲率小于1e-79；不能把这个结论替代有限warp的连续曲率核验。

同时W_n→0、B_n→0，径向图的w和w_r在r_c处趋零，
从而旋转背景C²接上r≤r_c的平圆盘。剩余高度由W_N乘剩余径宽控制；
本题N160的严格粗界小于1e-131。

复算：`python scripts/closing_deep_background_rational.py notes/closing_deep_background_n160_rational.json`。
这个背景结论对K6、K8、K9的浅层改变都适用，但不证明其非旋转修正仍有这些曲率界。
