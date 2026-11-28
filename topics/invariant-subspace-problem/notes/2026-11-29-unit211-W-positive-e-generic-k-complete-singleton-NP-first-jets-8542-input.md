# 新输入：正 e 一般 k 图的完整 singleton N/P 首阶原式

日期：2026-11-29（Asia/Taipei）；会话 Astra-ISP-8542378f-20261127。

**未执行的新原输入。** 自含；唯一绝对 120 秒、1 GiB，外层135秒。只构造四个新的完整原值 jet 及三个预定 f 结式，不重跑旧 q2/R6/N5 投影、83e六射线初始理想或任何冻结门。

源：2026-11-29-unit211-W-positive-e-generic-k-complete-singleton-NP-first-jets-8542.py。
SHA-256：958f1bbbf613211a047bb2adf91d340c8fd3ed23b5794470dee3f4d0ba9cfc5a。

## 1. 准确原范围

当前剩余特征1009的 W/b0 图，取
$$
v(e)>0,\quad v(k)=0,\quad \bar k\notin\{-2,-4,4\}.
$$
定义准确局部权坐标 $L=(k+2)/k$，故 $k=2/(L-1)$；在剩余域
$$
L(L-1)(2L-1)(2L-3)\ne0.
\tag{1}
$$
此前原证明已付 lambda 是单位、$\mu=2\lambda-3$ 整以及物理 f、sigma、完整Gram和两个物理值 h、k_val 都整：
[物理f整性与完整singleton模型](../results/R150-appendix-unit211-W-b0-positive-e-generic-unit-k-physical-f-integrality-and-singleton-model.md)。

特别 P02 的首项、D 或 G36 的首项均未被当作剩余单位。这里不添加任何 mu 或 f 首项的逆。

## 2. 精确的原一阶系数代数

源在
$$
\mathbb Q[L,\mu,f,(L(L-1)(2L-1)(2L-3))^{-1}][e]/(e^2)
$$
中按完整原定义运算。J(a,b)表示$a+be$，乘法严格为
$(a+be)(c+de)=ac+(ad+bc)e$；只有已付单位常数项的分母才求逆。这个 e 系数代数与原 Gram 的 dual 第一块是两个不同结构，代码分别处理。

保持
$$
u=1+e,\ Q=ek,\ \delta=1-Q,\quad
\ell=\frac{u((k+2)^2-2ek)}{k(uk+2)},\quad
m=u-\ell,\quad M=\ell^2\delta-m^2,\quad bc=M/(4\delta).
$$
原 b0 准确给
$$
T=\frac{u\ell\mu}{4u+2u/k-\ell},\qquad \lambda=(\mu+3)/2.
$$
原首阶恢复利用已经准确提取的 e 幂：
$$
T_0=e t_0,\quad t_0=-(2u+k\ell),\quad
\Phi=e^2\phi_2,\quad \phi_2=-2(k+4)/(uk+2),
$$
$$
P_{02}=e^2p_2,\quad
p_2=2u\{k^2+(5-2e)k+8\}/(uk+2),
$$
$$
G=e^2g_2,\quad g_2=\lambda p_2+t_0,\quad
P_c=e^3p_c,\quad p_c=kp_2(\ell+T)-g_2t_0.
$$
因此
$$
t_s=-p_c/(bc\,k\phi_2),\qquad
V_s=-eg_2/k-p_c/(k\phi_2),
$$
$$
\beta=2u-(\ell-2u/k),\quad
t=\beta f/(bc)+t_s,\quad V=2uf+V_s,\quad
W_1=e t_0/2+2uf.
\tag{2}
$$
x、y、A1 再由完整原仿射式恢复。所有出现的真正分母系数只含 (1)。

选 $\rho=1-ek/2\bmod e^2$，代码返回 $\rho^2=\delta$。这对应二次扩张中剩余为1的一支；另一支交换两个singleton，而两者原误差都保留。原权
$$
a=1-\ell,\quad b=(\ell+m/\rho)/2,\quad c=(\ell-m/\rho)/2
$$
及四行完整Gram直接恢复，不用旧压缩 mean 或任何曲线输出。

## 3. 四个新的同点原关系

完整原乘法的第一块为
$$
(vw)_0=v_0w_0,\qquad (vw)_1=v_0w_1+v_1w_0.
$$
设 $d=DK(\mathbf1)$、$F_2=\tau(d)$，源按原定义构造
$$
N_4(v)=2\tau(dv^2)-F_2\tau(v^2)
       -4\tau(v)\tau(dv)+2F_2\tau(v)^2+\tau(vDK(v)),
$$
$$
P_2(v)=\tau((v-\tau(v)\mathbf1)^3).
$$
分别记两singleton为B、C。此前纸面已完整给
$$
[N_B]_0=[P_B]_0,\qquad [P_C]_0=[N_C]_0=0.
\tag{3}
$$
本次由实际Gram系数代数再次返回 (3)，因此以下三个正幂除法确实正则：
$$
F_0=[P_B]_0,\quad
F_1=[(N_B-P_B)/e]_0,\quad
F_2^{\rm new}=[P_C/e]_0,\quad
F_3=[N_C/e]_0.
\tag{4}
$$
程序对应取一阶系数，无任何 e 逆运算。

原物理右侧是 $2\lambda P_{02}h^2$、$P_{02}h^3$ 及C的相应值。因为全部物理值已整、$P_{02}=e^2p_2$，这些项在 (4) 中的贡献全部为零。故每个实际原解必须在同一
$(\bar L,\bar\mu,\bar f)$ 上满足四式，而不是独立选择各个式的根。

四式关于(mu,f)的总次数至多三，f分母纯权。F0的f三次头完整返回
$$
[f^3]F_0=\frac{16(2L-2)(2L-3)}{(2L-1)^2},
$$
它在 (1) 上非零；这里用的是已证明的原P头，而不是事后泛域假设。

## 4. 事先固定的三个新来源结式

对三个固定组
$$
(F_0,F_1),\quad(F_0,F_2^{\rm new}),\quad(F_0,F_3)
$$
分别取固定f容量(3,3)的六阶Sylvester，不按实际结果改组或补列。若后一式的实际次数下降，容量保持；完整原坐标乘回覆盖所有下降面。

先清每个原式的已付纯权分母，记分子为 n_i。每个非零结式必须返回全部六个伴随坐标以及普通多项式身份
$$
A_j n_0+B_j n_j=C_j(L,\mu).
\tag{5}
$$
Bareiss每次精确除法都乘回，最终不倒任何主元或行列式。若某矩阵恒奇异，记录结式为零、保全部原纤维，不另换一个矩阵。

此后只从 C_j 中剥除 (1) 的已付支持，所有因子尺度一起运输回四个实际 F_i，完整返回
$$
\sum_{i=0}^3\Omega_{ji}F_i=\widetilde C_j(L,\mu).
\tag{6}
$$
最终原乘子的分母及有理系数逐项检查1009整性。没有添加mu头、f头或任何新权因子逆；所有未付头零支保留。

仅当(6)实际成为剩余特征1009单位，才可排除此图；一个非零多项式、有限次数或profile本身都不表示空性。三个新必要标量之间不计算gcd，也不重新执行原q2/R6/N5的旧结式。

## 5. 唯一执行边界

本源为新的完整原singleton正阶目标；旧源只作为纸面定义来源，不读取任何旧系数载荷或缓存。没有参数采样、数值根、改变素数或重复已成证书。

预定120秒/1GiB，三个组固定，任何资源边界后准确保存最后完整返回并冻结对应未完成目标；不增加预算或改组续跑。整正e射线、k负二有限中心、内部权图及DVR边界不由本输入预先关闭。
