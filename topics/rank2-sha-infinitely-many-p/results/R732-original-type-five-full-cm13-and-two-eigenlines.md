# R732 — 原 degree 34 型五空间的完整 CM13 算子与两条真实特征线

日期：2026-11-15。**状态：本篇完整证明原五维型五 theta 空间的特征零 CM13 算子、两条首项为 $z^5$ 的实际特征线、剩余不可约三维块及全部投影公式。两条线的完整算术角色、Katz 负一值与原冻结差测试的联系另行支付；本篇不以 CM 特征或正五阶系数代替负一单位矩非零。**

所用的是 [R728](R728-frozen-type-five-connection-and-complete-near-cancellation.md) 中出现的原五维空间。它不是 R307 的六维型一奇空间，也不是将协变导数视作与 CM 自动交换所得的替代空间。

## 1. 规范与完整结论

固定
$$
K=\mathbf Q(\omega),\qquad \omega^2+\omega+1=0,\qquad
\delta=1+2\omega,\quad \gamma=4+\omega,\quad E_b:y^2=x^3+b.
\tag{1}
$$
采用原规范
$$
x=z^{-2}+\cdots,\quad y=-z^{-3}+\cdots,\quad
\sigma=z+\cdots,\qquad X=x^3,
\tag{2}
$$
最后取 $b=17$。原始 CM 迹和归一算子是
$$
M=[\gamma]_*[\bar\gamma]^*,\qquad N=\gamma^{-1}M.
\tag{3}
$$
这里的 push 是全十三个逆像的实际迹，不除以 $13$，也不另添局部 Weil 标量。

**定理 1。** 整个标准 degree $34$、$\mu_6$ 型五空间为
$$
\mathcal H_{34,5}=-\sigma^{34}xy\,K[X]_{\le4}.
\tag{4}
$$
算子 (3) 保持此空间，其特征多项式和最小多项式均准确为
$$
\boxed{\det(T-N)=(T+1)(T+\omega^2)(T^3+\omega).}
\tag{5}
$$
特别 $N^{18}=I$。前两个特征空间各为一维，其唯一首项 $z^5$ 规范分别是
$$
\begin{aligned}
D_{-,b}={}&-\sigma^{34}xy
 \bigl(X^4+13bX^3-156b^2X^2-104b^3X+64b^4\bigr),\\
D_{\omega,b}={}&-\frac1{11}\sigma^{34}xy
 \bigl(11X^4-109bX^3+120b^2X^2+368b^3X+128b^4\bigr).
\end{aligned}
\tag{6}
$$
其绝对原始迹特征为
$$
\boxed{MD_{-,b}=-\gamma D_{-,b},\qquad
MD_{\omega,b}=-\gamma\omega^2D_{\omega,b}.}
\tag{7}
$$
剩余三维空间的最小多项式是 $T^3+\omega$，在 $K$ 上不可约；它完整保留，未被当作质量零或未知角色而删除。

每个来源都有唯一分解
$$
F=P_-F+P_\omega F+P_{\rm prim}F,
\tag{8}
$$
其中真正作用于同一原来源的完整算子为
$$
\begin{aligned}
P_6&=\frac{N^3+\omega I}{\omega-1},&
P_-&=\frac{N+\omega^2I}{\omega^2-1}P_6,\\
P_\omega&=\frac{N+I}{1-\omega^2}P_6,&
P_{\rm prim}&=I-P_6.
\end{aligned}
\tag{9}
$$
因此 $P_-F\in KD_{-,b}$、$P_\omega F\in KD_{\omega,b}$。这些是全纤维算子的多项式；若用于实际混合单位域，仍须逐项运输各个 CM 分支及全部伴随，不能只保边际上的多项式投影。

## 2. 为什么全局空间恰为五维

除以 $\sigma^{34}$ 后，标准 theta 截面给在 $O$ 以外无极、在 $O$ 极阶至多 $34$ 的椭圆函数。基可取 $x^a$、$x^ay$，分别满足 $2a\le34$、$2a+3\le34$。

对 $u\in\mu_6$，
$$
\sigma(uz)=u\sigma(z),\quad
x(uz)=u^{-2}x(z),\quad y(uz)=u^{-3}y(z).
\tag{10}
$$
型五要求 $34-2a-3\equiv5\pmod6$，故奇基中准确是 $a=1,4,7,10,13$；偶基没有型五。因此 (4) 是整个空间，而非一个候选子空间。

真实 CM pull/trace 保持标准 degree $34$ 的 theta 结构，并与 $\mu_6$ 作用交换。这里的 theta 结构、odd norm 的半特征和原准周期正是 [R297](R297-jzero-actual-cm13-mass-kernel-cm7-product-and-angular-source.md) §2–3 的规范。于是输出仍必在 (4)。随后只在这个已知完整五维空间中用五个全纤维求值确定全局算子。

## 3. 全十三纤维的准确有理式

先取 $b=1$。R297 已付的实际 sigma division 多项式为
$$
Q(x)=\frac{\sigma(\gamma z)}{\sigma(z)^{13}}
=\gamma\left(x^6+(8+12\omega)x^3+\frac{64+48\omega}{13}\right),
\qquad \bar Q=\overline Q.
\tag{11}
$$
必须保留前导系数 $\gamma$；用首一多项式替换 (11) 会改变原迹的绝对相位。

记撇号为 $x$ 导数，设
$$
\begin{aligned}
A_\gamma&=13xQ^2
 -4(x^3+1)(Q''Q-(Q')^2)-6x^2Q'Q,\\
B_\gamma&=\gamma^2Q^2,\qquad X_\gamma=A_\gamma/B_\gamma.
\end{aligned}
\tag{12}
$$
则 $X_\gamma=x(\gamma z)$。对共轭方向定义 $X_{\bar\gamma}$ 同理。目标横坐标为 $a$ 时，令
$$
f_a=(A_\gamma-aB_\gamma)^{\rm monic},\qquad
x_b=X_{\bar\gamma}\quad\text{于 }K[x]/(f_a).
\tag{13}
$$
选用的每个 $f_a$ 都是可分十三次多项式，所用分母在商环中可逆。

奇来源还必须保留纵坐标比。由 $x'(z)=2y(z)$，
$$
X_\gamma'(x)=\frac{\gamma y(\gamma z)}{y(z)},\qquad
\boxed{\frac{y(\bar\gamma z)}{y(\gamma z)}
=\frac{\gamma}{\bar\gamma}
 \frac{X_{\bar\gamma}'(x)}{X_\gamma'(x)}=:r_y.}
\tag{14}
$$
这正是实际 $y$ 比，不能只取两条 $x$ 有理函数来计算型五迹。

取没有额外列缩放的基
$$
e_j=-\sigma^{34}xyX^j,\qquad 0\le j\le4.
\tag{15}
$$
将 $Me_j$ 除以目标的 $-\sigma^{34}y$，得到完整纤维公式
$$
\boxed{
\operatorname{Tr}_{f_a}
 \left[(\bar Q/Q)^{34}r_y x_b^{\,1+3j}\right].
}
\tag{16}
$$
它包括十三个实际逆像；目标 $y$ 已在 (14) 除掉，没有额外的二倍或二分之一。对首一 $f_a$，全迹准确等于
$$
[x^{12}]
 \left(\bigl[(\bar Q/Q)^{34}r_y x_b^{\,1+3j}\bigr]f_a'
             \bmod f_a\right).
\tag{17}
$$

令 $a=2,3,4,5,6$。五个输出的系数由求值矩阵
$$
V_{a,i}=a^{1+3i},\qquad 0\le i\le4
\tag{18}
$$
唯一确定，因为
$$
\det V=\left(\prod_{a=2}^{6}a\right)
       \prod_{2\le a<a'\le6}(a'^3-a^3)\ne0.
\tag{19}
$$
(16)–(19) 因此给完整全局算子，不依赖用有限数值点猜测 theta 恒等式。另两个全纤维 $a=7,8$ 由脚本逐列验证相同矩阵。

在每个相同全纤维中，还原样计算原
$$
S=\sigma^{34}x^2
 \left(X^4-\frac{53}7X^3-\frac{12}7X^2-\frac{80}7X-\frac{128}7\right)
\tag{20}
$$
并核定 $MS=-\gamma S$。这与 R297 的原始迹完全一致，付清 (7) 的绝对定标；没有将一个仅与原迹 projectively 相同的有限矩阵代入。

## 4. 特征零的矩阵等式与三维余块

算法只在 $K=\mathbf Q(\omega)$ 中作四则运算、商环 Euclidean 求逆与多项式余式。由 (16)–(19) 得到 $M$ 后除以 $\gamma$，其准确特征多项式按降幂为
$$
T^5-\omega T^4+\omega^2T^3+\omega T^2-\omega^2T+1.
\tag{21}
$$
它等于 (5)。将下列两列直接代入同一个矩阵，分别得到 $-1$、$-\omega^2$ 倍：
$$
v_-=(64,-104,-156,13,1)^{\mathsf t},\qquad
v_\omega=\frac1{11}(128,368,120,-109,11)^{\mathsf t}.
\tag{22}
$$
所有 (21)、(22) 及 $N^{18}=I$ 都是特征零有理恒等式，由完整 producer 重建并验证，不是某个辅助素数模约化的相容性。

多项式 $T^3+\omega$ 的根是原始十八次单位根中对应的一组三个根；若它在 $K$ 上有根，$K$ 就会包含一个次数为六的原始十八次分圆数，矛盾。因此该三次因子在 $K$ 上不可约，且与 $T+1,T+\omega^2$ 互素。由 (21) 可知矩阵可分、三个直和块维数依次为 $1,1,3$，最小多项式必等于特征多项式。(9) 正是这三个互素因子的准确 CRT 投影。

(15) 中最高列首项是 $z^5$，(22) 的最高列系数均为一，因此 (6) 的首项准确为 $z^5$。用固定六次缩放
$$
D_{\bullet,b}(z)=b^{-5/6}D_{\bullet,1}(b^{1/6}z)
\tag{23}
$$
回到 $b=17$，得到 (6) 的全部 $b$ 幂及 (7)。该缩放与两个固定 CM 乘法严格交换。定理 1 得证。

## 5. 对当前原负一问题的确切含义

R728 的五个型五来源和本篇 (4) 是同一个完整空间；基只差显示的固定 $b$ 幂和列顺序。因此，对当前真实冻结差 $D_N(0)$，(8) 是合法的完整来源分解，包含两条 (6) 及一个真实三维余项。

本篇尚未证明 $D_N(0)$ 的三维余项为零，也未把五维负一矩识别为两条线的值。特别：

- (6) 的正五阶系数非零不等于其单位负一矩非零；
- (9) 用于原混合域时是实际有限 CM 全迹，不能与原 $Y/W$ 单位条件、两条斜门或五个隐藏条件免费交换；
- 原协变导数中的 $\sigma'(P/\sigma)$ 仍按 R728 的同源两输入卷积保留；本篇不宣称 CM 与这个协变导数交换；
- 剩余 $T^3+\omega$ 块没有被赋予原三条合格曲线的中央零，原外部相反补偿亦未删除。

两条 (6) 的完整有限 Schwartz 角色、共同 period、负一 Katz 点与解析秩一论证将接续处理。当前结论已经把原五维来源的有限算子及全部谱块精确固定，无需等待后续算术部分才成立。

## 6. 可重现的公开执行

唯一 producer 是
[check-r732-original-type-five-cm13.py](../scripts/check-r732-original-type-five-cm13.py)，它从 (11) 重建所有有理式、七个全纤维及完整矩阵，不读生成数据或旧 JSON。

- 公开 workflow：rank2-sha-r732-type-five-cm13。
- source commit：1d65f51bbecf16d17c2ef4790e5c1c50a20bf282。
- run：43701604983；job：132773743300。
- 命令：python check-r732-original-type-five-cm13.py --workers=4。
- 环境：python-flint==0.9.0。
- 脚本 SHA256：d1b3c2f851e9ec6b6d6b6655141e36b4bb1108a30e57ff8365b5f583d880e469。
- stdout：1676 字节；SHA256：f1ad231f2deb21fdb39fa4e88ab40c2d8cecc489c033557e9b956307caeb99a5。

运行完成全部精确断言。生成矩阵及输出可由脚本重算，依根 README 第 15 条不另存生成数据。
