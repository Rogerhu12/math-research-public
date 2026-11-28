# h=k：新的完整个别 N/P 与不除 NV 斜率的原标量返回

日期：2026-11-28（Asia/Taipei）。会话 Astra-ISP-8542378f-20261127。AI-assisted，GPT-6 Astra Pro。

冻结源：2026-11-28-unit211-h-equals-k-corrected-individual-NP-NV-scalar-returns-8542.py。
Git blob bb534b16c2858c7cec98c5358ca105758e736e67；10461 字节；
SHA256 00d513d603f862ef6b484176fe4d9da3b766e0047d46a87ec8f575622aa8ca14。
首次固定 180 秒 / 4 GiB。本文只登记新输入，尚不声称执行成功或原图排空。

## 1. 准确原图与唯一成功前缀

沿[正确五原行与三物理必要条件](../results/R150-appendix-unit211-h-equals-k-corrected-five-original-rows-and-three-physical-cofactor-conditions.md)
的同一个 $ABQ(1-Q)P_f\ne0$ 坐标图，保持原 $bcP_{02}\ne0$。
其中
$$
A=2\lambda^2-2\lambda+1,\quad B=4\lambda^3-6\lambda^2+3\lambda-1,
\quad \xi=B/A,\quad \ell=A^3/B^2,\quad T=A^2/B,
$$
$$
h=k=1+\xi,\quad w=\lambda-1-T,\quad \delta=1-Q,\quad m=u-\ell,
\quad bc=\frac{\ell^2-m^2/\delta}{4},\quad M=4bc\delta.
$$
只读取正确 f33 源的坐标定义前缀，截止唯一标记
`# Exact scalar forms` 之前：4540 字节，SHA256
a56e54b840cc323675394f96484c99658cad9a8420933cd2f344fe2df0d76efc。
不执行原五行、三 cofactor 或因式分解尾，不执行旧错误 compact 源。

$f,z$、$v_n,W_*$、$NV$ 直接复用该前缀中的**参数定义**；
$f$ 已由原 $P_1$ 在 $P_f$ 上消去。$\Delta=0$ 完整保留。

## 2. 同一原 Gram 的完整恢复

设
$$
V=v_n/Q,\quad W=W_*/2,\quad t=z/Q,\qquad
x=\frac{(u-\ell Q)V-mW}{M},\quad
y=\frac{\ell W-uV}{M}.
$$
在完整二次代数 $\rho^2=\delta$ 上取
$$
p=1+\rho,\quad q=1-\rho,\quad
b=\ell/2+\rho m/(2\delta),\quad c=\ell/2-\rho m/(2\delta),
$$
$$
X=x+\rho y,\quad Y=x-\rho y,\quad
r=X-(1-\ell)p-ct,\quad s=Y-(1-\ell)q-bt,
\quad A_1=2f-2V+2bc\,t.
$$
由四行
$$
(0,0,p,q),\quad(0,A_1,r,s),\quad(p,r,0,t),\quad(q,s,t,0)
$$
和真正 dual 乘法定义全部原量。源将完整返回原 $E_0,N_0,P_0,P_1$、
$V_{\rm val}=(1,w,h,h)$ 的前三矩，以及
$$
Q N_4(V_{\rm val})=2NV.
$$
不选择一个 $\rho$ 根；同一点同时保留 B、C 条件。

## 3. 四个真正新原值条件

本次新输入是
$$
N_4(g_B)-2\lambda P_{02}h^2,\quad
N_4(g_C)-2\lambda P_{02}h^2,
$$
$$
P_2(g_B)-P_{02}h^3,\quad P_2(g_C)-P_{02}h^3.
$$
共轭两式同时为零且 $\rho\ne0$，给完整偶、奇四行
$NBe,NBo,PBe,PBo$；它们都是 $z$ 至多三次多项式。
这不是单个选定 $\rho$ 根为零就强迫全部系数为零。

只清除命名坐标单位 $A,B,Q,\delta,P_f$ 和实际物理单位
$M=4bc\delta,P_{02},\lambda,2\lambda-1$。
$\lambda$ 来自已经排空零孤立 mean 后的 $m_{\rm isolated}/U_0$；
$2\lambda-1$ 来自独立 347c 原五列物理秩排除。
后者不是裸均值理想的单位证书，不能抹掉其物理前提。
所有其它权因子、$\Delta$ 和新斜率都不倒置。

## 4. 保留 NV 斜率为零的完整原身份

在同一原单位清式后写 $NV=b_0+a_0z$。
对四个新三次 $P(z)=\sum_{j=0}^3P_jz^j$，定义
$$
R_P=\sum_{j=0}^3P_j(-b_0)^j a_0^{3-j}.
$$
源将完整返回
$$
\boxed{a_0^3P(z)-R_P=(b_0+a_0z)
 \sum_{j=1}^3P_j\sum_{k=0}^{j-1}a_0^{2-k}(-b_0)^kz^{j-1-k}.}
$$
这是四个 $z$ 系数逐项的多项式身份，包含 $a_0=0$；
没有以有理代入 $z=-b_0/a_0$ 丢失零斜率支。
因此原点必要满足四条 $R_P=0$。
仅删除已付物理因子，完整乘回并分解剩余原必要标量。

新目标仅为四条原标量返回、其准确次数/因子与来源；
不从多变量 gcd 或因式分解宣称共同零集为空。
若首次门失败，保最后实际阶段，不增加资源、重排行序或接算旧门。
源码和小执行回执保留可再生定义，不保存展开系数缓存。
