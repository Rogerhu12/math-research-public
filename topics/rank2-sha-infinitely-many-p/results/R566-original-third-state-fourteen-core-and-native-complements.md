# R566 — 完整第三态十四度核心与两个 native 补域的五观察返回

日期：2026-11-14。**状态：已证明。**

R563 的第三态不必回到旧 $c$–$C$ 小 gluing 格。
在一个完整整数框架中，它仍保原 $D_{14}=F-C$ 的整个
$\mathcal S_{14}$，因此该轴的真实 scalar 核 $\beta$ 对全部三态成立。

这使 R563 的两个真正互补积分都能回到 R560 的原五观察空间：
$D_{12}$ 单位一项准确对应 $14X-E$ 单位，$D_{12}$ 深一项
准确对应 $14X-E$ 深。第三态由完整 $K$ 单位逆消去，未赋其
中央零；两个原条带、原 $Y/W$ 权及所有 log 质量均保留。

## 1. 同一个来源及两个不同的 D

沿用 [R559](R559-original-plane12-square-core-and-native-one-sided-carry.md)、
[R560](R560-native-single-branch-and-seven-conditional-moments.md)、
[R563](R563-original-s24-three-state-and-native-unit-complement.md)
的全部射线、固定坏集与原周期：
$$
\omega^2+\omega+1=0,\quad\delta=1+2\omega,\quad b=17,\quad
\lambda=-\bar\pi_0^{-1},\quad\beta=-\lambda,\quad
\kappa=p\lambda^2,\quad p\ge71 .
\tag{1}
$$
原六输入为 $(\xi_1,\xi_2,\xi_3,x,c,d_0)$，原两态
$\rho_0,\eta$ 与 $h=\eta+\rho_0/2$ 不变。
设
$$
C=(\xi_1-\xi_3+x)/\delta,\quad
D_4=\xi_1+\omega^2\xi_2-2\omega\xi_3,\quad
F=D_4+C+c+(2+3\omega)d_0 .
$$
本篇明确区分
$$
\boxed{D=F-C,\quad N(D)=14;\qquad A=F-c,\quad N(A)=12.}
\tag{2}
$$
$D$ 是 R560 的原 carry 轴，$A$ 是 R559/R563 的 $D_{12}$。
另设
$$
H=\delta(c-C),\quad K=\delta(c+C),\quad R=2\delta A .
$$
真实恒等式为
$$
\boxed{D=A+H/\delta,\qquad D\perp K.}
\tag{3}
$$

保 R563 的完整三态
$$
\mu_0=\mathcal P_C\rho_0,\qquad
\mu_+=\mathcal P_Ch,\qquad
\mu_-=K_H\mu_+=-K_K\mu_+,\qquad
\boldsymbol\mu=(\mu_0,\mu_+,\mu_-)^t .
\tag{4}
$$
$K_H,K_K$ 都已经提出外部 $\lambda$。
这里的纯 $C$ 投影与反射、原来源定义均与 R559 相同。

## 2. 保 D14 的完整整数框架

令
$$
\bar H=H-\frac{\delta}{7}D,\qquad
Q=R-12H=-14\bar H .
\tag{5}
$$
直接计算有
$$
N(\bar H)=36/7,\qquad N(Q)=1008,\qquad
D,\ K,\ Q\text{ 两两正交}.
$$
取 R563 原四个伴随中的同一 $T_1,T_2,T_3$，完整新 frame 是
$$
\boxed{(D,\,2K,\,Q,\,2T_1,\,2T_2,\,2T_3).}
\tag{6}
$$
它相对 R563 的 $(2H,2K,R,2T_1,2T_2,2T_3)$ 行列式因子为
$7/(2\delta)$，因此
$$
\det=1992646656+5615640576\omega,\qquad
N(\det)=2^{26}3^{11}7^2\,13^3\,19 .
\tag{7}
$$
这是当前处完整可逆的整坐标变换。

(6) 的前三轴与后三个 $T$ 正交，前三轴 degree 依次为
$14,24,1008$。还须检查真正的来源格，而不只计算 Gram：
对纯 $C$ 旋转的三支，$D$ 分别成为原三个
$D_j=F-\omega^{2j}C$，全部为整数 even 行。
$2K$ 的前三个 $H_0$ 系数只乘三次单位，仍是整数；
$Q=R-12H$ 中 $R$ 固定，$12H$ 的每支同样整。
再乘原 $\eta$ 的实际二输入矩阵 $\mathsf H$，这些行仍为整数，
前三轴的半特征均为 standard even。
后三个 $2T$ 原样保留，仍清掉原半系数。
配套证书保存三支的全部这些行和各自奇因子个数。

因此在此完整框架中
$$
\mu_0,\mu_+\in
\mathcal S_{14}(D)\otimes\mathcal S_{24}(2K)
\otimes\mathcal S_{1008}(Q)\otimes\mathcal T_{\rm rem}.
\tag{8}
$$
$\mathcal T_{\rm rem}$ 包含真实三个伴随的全部耦合。
按定义 $\mu_-=-K_K\mu_+$；$K_K$ 只操作 (8) 的第二轴，
故它保持第一轴的**整个** $\mathcal S_{14}$。
这严格支付了 $\mu_-$ 的十四度身份，没有假设它仍属于
旧 $\mathcal S_4(c)\otimes\mathcal S_3(H_0)$ 小格。

R560 已付原 standard even $\mathcal S_{14}$ 的完整核心
$\beta=-\lambda$。由 (8)，对全部三态、全部 $n\ge0$ 都有
$$
\boxed{
\boldsymbol\mu|_{\{D\in p^n\}}
=\beta^n(P_{D,\kappa^n})_*\boldsymbol\mu .
}
\tag{9}
$$
也可由 $D\perp K$、$\mu_-=-K_K\mu_+$ 和完整 trace 交换直接核定：
$(K_DK_K)\mu_+=(K_KK_D)\mu_+$。绝对标量没有改变。

## 3. 原五观察及真实投影超平面

记 R560 的原
$$
E=F+13C=D+14C,\qquad
\pi_5=(E,Y,W,W',G),
$$
$$
X=c-D/14,\qquad Z=d_0+(1+3\omega)D/14,\qquad a_0=2+\omega .
\tag{10}
$$
这些五个观察与 $D$ 全部正交，$(D,\pi_5)$ 为原完整可逆框架。
由 (3)、(5)、(10) 准确有
$$
\boxed{\bar H=\delta(X-E/14),\qquad E=7(K-\bar H)/\delta.}
\tag{11}
$$
所以 $\bar H$ 是原 $\pi_5$ 的一个实际线性式。
若要完全展开，R560 的原逆矩阵给
$$
\begin{aligned}
14X-E={}&-\frac{12}{13}E+
\frac{7(13+27\delta)}{144}Y
-\frac{285+575\delta}{432}W\\
&+\frac{75+71\delta}{432}W'
+\frac{7(4+\delta)}{468}G .
\end{aligned}
\tag{12}
$$
它不是新添加的独立自由变量。

在 $P_{D,\kappa^n}$ 下，保持 $K,\bar H,T$ 不动，
$$
\boxed{
\begin{aligned}
H&\longmapsto \bar H+\delta\kappa^nD/7,\\
A&\longmapsto -\bar H/\delta+6\kappa^nD/7,\\
C&\longmapsto E/14-\kappa^nD/14 .
\end{aligned}}
\tag{13}
$$
于是对 $n\ge1$，
$$
H\text{ unit}\Longleftrightarrow \bar H\text{ unit}
\Longleftrightarrow A\text{ unit},
\qquad C\text{ unit}\Longleftrightarrow E\text{ unit}
$$
均是在该真实缩放后的准确事件等价。原 $Y,W,E,G$ 完全没有移动，
所以这里没有隐藏的尺度 log。

## 4. 同一个 native 测试的准确归一

以下 $\widehat P_p$ 始终是 R536 的原七行右逆所得六次多项式，
所有 $p,\lambda,\kappa$ 系数原样保留。定义
$$
\ell=(p-1)\{1_{Y\text{ unit}}\log\langle Y\rangle
-1_{W\text{ unit}}\log\langle W\rangle\}.
$$
令 $\mathcal B,\mathcal B^c$ 是 R559/R563 的原两个条带，
$\mathcal E_n=\{D\in p^n,C\text{ unit}\}$。
R563 的原三列测试是
$$
f_n=
\frac{1_{\mathcal E_n}}{b\Omega^6}
\widehat P_p(D/\kappa^n,E,G)\,\ell
\begin{pmatrix}
\tfrac32(1_{\mathcal B}+1_{\mathcal B^c})\\
1_{\mathcal B^c}-1_{\mathcal B}\\0
\end{pmatrix}.
\tag{14}
$$
其完整积分仍是原 residual
$\mathcal N_n=2\lambda h(\Phi_1-\Phi_2)$。

R560 准确证明
$$
P_{D,\kappa^n}^{-1}\mathcal B=\mathcal B_+
=\{Z\text{ unit},X-a_0Z\in p\},
$$
$$
P_{D,\kappa^n}^{-1}\mathcal B^c=\mathcal B_-
=\{Z\text{ unit},X+a_0Z\in p\}.
\tag{15}
$$
两域不交。这些都是 $\pi_5$ 的实际事件。

置与 $n$ 无关的完整三列函数
$$
\boxed{
f^\flat=
\frac{1_{E\text{ unit}}}{b\Omega^6}
\widehat P_p(D,E,G)\,\ell
\begin{pmatrix}
\tfrac32(1_{\mathcal B_+}+1_{\mathcal B_-})\\
1_{\mathcal B_-}-1_{\mathcal B_+}\\0
\end{pmatrix}.
}
\tag{16}
$$
由 (13)–(15)，整个原输入空间上有
$$
\boxed{f_n\circ P_{D,\kappa^n}=f^\flat,\qquad n\ge1.}
\tag{17}
$$
第一多项式变量 $D/\kappa^n$ 准确返回 $D$。
所有原单位条件和两个独立的 log 已经包含在 (17)，
不是只对一个正矩或一个角型的等式。
由 (9)，
$$
\mathcal N_n=\beta^n\langle f^\flat,\boldsymbol\mu\rangle .
\tag{18}
$$

## 5. K 侧真实补域完整返回

用 R563 的对称来源矩阵
$$
A_K=\begin{pmatrix}-1&0&0\\0&0&-1\\0&-1&0\end{pmatrix}
$$
和其已付完整连续逆
$\mathcal U_K=(I-\lambda A_KS_K)^{-1}$。
它包含 R563 (20) 的整常数逆及全部连续差级数，不是形式几何级数。
令 $\mathcal U=\{H,K\text{ unit}\}$。R563 的两个实际项为
$$
\mathcal N_{K,n}=
\left\langle1_{\mathcal U\cap\{A\text{ unit}\}}\mathcal U_Kf_n,
\boldsymbol\mu\right\rangle ,
$$
$$
\mathcal N_{H,n}=
\left\langle1_{\mathcal U\cap\{A\in p\}}\mathcal U_Hf_n,
\boldsymbol\mu\right\rangle ,
\quad
\mathcal N_n=\mathcal N_{K,n}+\mathcal N_{H,n}.
\tag{19}
$$

$D\perp K$ 给两条真实交换：
$P_{D,\kappa^n}$ 与 $S_K$ 交换，且与 $K=0$ 的连续极限交换。
故它与整个 $\mathcal U_K$ 交换。
又 $f_n$ 支撑于 $D\in p^n$，$K$ 缩放不改变 $D$，
所以 $\mathcal U_Kf_n$ 也具有该完整支撑。

对 $\mathcal N_{K,n}$ 使用 (9)、(13)、(17)，准确得到
$$
\mathcal N_{K,n}
=\beta^n
\left\langle1_{\{\bar H,K\text{ unit}\}}\mathcal U_Kf^\flat,
\boldsymbol\mu\right\rangle .
\tag{20}
$$
$\bar H\perp K$，所以 $1_{\bar H\text{ unit}}$ 是 $K$ 独立事件，
与单位逆的每一项和常数项都交换。
应用 R563 的完整 $K$ 单位返回即得
$$
\boxed{
\mathcal N_{K,n}
=\beta^n\left\langle1_{\{\bar H\text{ unit}\}}f^\flat,
\boldsymbol\mu\right\rangle .
}
\tag{21}
$$
由于 $f^\flat$ 第三列为零，(21) 最右边只含原
$\mu_0,\mu_+$。$\mu_-$ 是由完整逆准确消去，不是因其质量为零、
反射奇性或某个未付小格身份消失。

(21) 还保留原 $E$ 单位、$\mathcal B_\pm$、分别的 $Y/W$ 单位条件
及两 log 质量；这一步没有做任何首阶近似。

## 6. H 侧深补域及完整五观察分区

从完整 (18) 减去已经完整支付的 (21)，而非丢弃另一域，得
$$
\boxed{
\mathcal N_{H,n}
=\beta^n\left\langle1_{\{\bar H\in p\}}f^\flat,
\boldsymbol\mu\right\rangle .
}
\tag{22}
$$
这是整个受限积分的等式。它不宣称 R563 的 $A$ 深域与
$\bar H$ 深域是原坐标中同一个集合，也不宣称每个逆级数项
可逐点这样换域。实际论证是先对完整 $K$ 侧付 (20)–(21)，
再用无遗漏的两项分区。

用 R560 的原两条完整五变量测度
$$
\mathfrak M_\mu=(\pi_5)_*\{\widehat P_p(D,E,G)\mu\},
\qquad\mu=\mu_0,\mu_+,
$$
定义同一个实际五变量积分核
$$
d\mathfrak L=
1_{E\text{ unit}}\ell
\left\{
\tfrac32(1_{\mathcal B_+}+1_{\mathcal B_-})\,d\mathfrak M_{\mu_0}
+(1_{\mathcal B_-}-1_{\mathcal B_+})\,d\mathfrak M_{\mu_+}
\right\}.
\tag{23}
$$
则两个真正补域的最终式为
$$
\boxed{
\mathcal N_{K,n}=
\frac{\beta^n}{b\Omega^6}
\int_{\{14X-E\text{ unit}\}}d\mathfrak L,\qquad
\mathcal N_{H,n}=
\frac{\beta^n}{b\Omega^6}
\int_{\{14X-E\in p\}}d\mathfrak L .
}
\tag{24}
$$
两项各自除了显式 $\beta^n$ 外都不依赖 $n$。
与 R560 的七个条件源展开结合，(24) 是原来源内的完整有限表达。
尤其第六矩中的 $-672b\Omega^6\Lambda_{\mu,0}$ 仍在，
没有省去真实质量。

在两个原条带内，第二个超平面还可准确写成
$$
\begin{array}{ll}
\mathcal B_+:&E-14a_0Z\in p,\\
\mathcal B_-:&E+14a_0Z\in p .
\end{array}
\tag{25}
$$
这是由 $X\mp a_0Z$ 已深得到的事件等价，不把 $E$ 或 $Z$
另取独立深度。它保同一个五变量来源和所有原观察。

## 7. 当前边界及证书

(9) 是对完整第三态的真实十四度核心。
(21)–(24) 则把 R563 的两条原 native 补偿各自准确回接到原
$\pi_5$ 条件行，并完整消去单位逆中产生的第三态。
本篇没有给两项分别赋零，也没有由 R558 的另一个深网格零质量
删去 (23) 的常数 log。原算术条件仍须通过已支付的对应测试使用；
主目标没有因此完成。

- [check-r566-original-third-state-fourteen-core-and-native-complements.js](../scripts/check-r566-original-third-state-fourteen-core-and-native-complements.js)
- [check-r566-original-third-state-fourteen-core-and-native-complements.json](../scripts/check-r566-original-third-state-fourteen-core-and-native-complements.json)

精确脚本用 BigInt 有理 CM 算术保存完整新 frame、全部三支原/η
整数行及其半特征、行列式、观察正交关系和 (11)–(13)。
完整连续逆和实际域的论证由 (17)–(24) 给出，没有另加采样验证。
