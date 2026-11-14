# 实际中央行的整主部、Picard–Fuchs 消元与固定权三留数线

日期：2026-11-12。状态：首层中央系数的整主部模型、精确
Picard–Fuchs/Bol 分解、固定 CM 留数格与高极点阶乘成本均已证明。
没有证明所选主部模型继承原 level \(68\) 形式的全部 Hecke 关系，
也没有得到新的无穷素数非零结论。

## 1. 同一个实际中央系数

沿用[全权一 GM 临界行](2026-11-12-full-weight-one-gm-critical-rows.md)
及[真实整 Frobenius](2026-11-12-integral-gm-frobenius-critical-row.md)：

\[
t=\lambda-\tfrac12,\qquad s=1-4t^2,\qquad
\mathscr D=(s\partial_t)'-1
          =s\partial_t^2-8t\partial_t-1,
\]
\[
\mathscr DK=\mathscr DL=0,\quad
K(0)=L'(0)=1,\quad K'(0)=L(0)=0,\quad
J=L/t,\quad KL'-K'L=s^{-1}.
\tag{1}
\]

实际固定代数函数为
\[
M=M_e=t^4+\tfrac72t^6+\cdots,\qquad
M\in\mathbb Z_p[[t]]
\quad\bigl(p\notin\{2,3,5,17\}\bigr).
\tag{2}
\]
它不是另选的辅助模函数。取惰性 \(p\ge7\)，置 \(d=p+1\)。
准确的实际中央系数及其首层为
\[
C_d=\operatorname{res}_{t=0}
       \frac{MK^d}{sL^{d+1}}\,dt,\qquad
\Gamma_{i,p}=C_d/p\in\mathbb Z_p.
\tag{3}
\]
已有的平方公式是
\[
C_d=\frac{d!}{24\,17^{d-4}}\beta_d^2,\qquad
\beta_d=[z^d]A_1(z)\in\mathbb Z_p.
\tag{4}
\]
所以 \(\Gamma_{i,p}\bmod p\ne0\) 准确等价于 \(\beta_d\) 是单位；
这仍是 R50/R54 的初级有限性充分条件。

以下 \([F]_{\le n}\) 表示 \(F\) 在原点的次数至多 \(n\) 的截断。
定义
\[
\boxed{\quad
 f_p(t)=t^{-p-2}
 \left[\frac{M(t)K(t)^p}{s(t)J(t)^{p+2}}\right]_{\le p+1}.
\quad}
\tag{5}
\]
这是真正的有限 Laurent 多项式。由 \(M\) 的四阶零点，
计算 (5) 只需 \(K,J\) 的次数至多 \(p-3\) 的系数。
这些系数的递推分母都小于 \(p\)，故
\[
f_p\in t^{-1}\mathbb Z_p[t^{-2}],\qquad
\operatorname{pole}_0(f_p)=p-2,\qquad
[t^{-p+2}]f_p=1.
\tag{6}
\]
这里最高极点是 \(p-2\)，没有把未消去四阶零点的 \(p+2\)
误用于整性判断。

取真实整基 \(e=(\omega,\eta)^T\)，其中
\(\omega=dx/(2y)\)、\(\eta=\nabla_{\partial_t}\omega\)。
原点初值为单位矩阵的水平基为
\[
h=Y^{-1}e,\qquad
Y=\begin{pmatrix}K&L\\K'&L'\end{pmatrix}.
\]
于是 \(\omega=Kh_1+Lh_2\)，所以 \(f_p\omega\,dt\) 的水平留数为
\[
\boxed{\quad
\operatorname{Res}_0(f_p\omega\,dt)=(C_d,0).
\quad}
\tag{7}
\]
第一坐标由 (3)、(5) 直接得到；第二坐标为零，因为
\(f_p\) 与 \(L\) 都是奇函数，\(Lf_p\) 是偶 Laurent 多项式。
被截去的正次数部分乘 \(K\) 或 \(L\) 都不能产生留数。

## 2. 无 \(p\) 损失的显式消元

连接矩阵是
\[
\nabla_{\partial_t}
\binom{\omega}{\eta}
=
\begin{pmatrix}0&1\\s^{-1}&8t\,s^{-1}\end{pmatrix}
\binom{\omega}{\eta}.
\]
对任意有理函数 \(R\) 直接微分得
\[
\boxed{\quad
\nabla(-sR'\omega+sR\eta)
       =-\mathscr D(R)\,\omega\,dt.
\quad}
\tag{8}
\]
关键单项式公式为
\[
\mathscr D(t^n)=n(n-1)t^{n-2}-(2n+1)^2t^n.
\tag{9}
\]

从 \(f_p\) 的最高负奇幂向上逐项消去。若当前项为
\(c\,t^{-(m+2)}\)，其中 \(m\) 为正奇数，则减去
\[
\mathscr D\left(\frac{c}{m(m+1)}t^{-m}\right)
\]
消掉它，只会改变低两个极点阶的 \(t^{-m}\) 项。
本次出现的 \(m\) 全在
\[
1,3,\ldots,p-4.
\]
因此每个 \(m(m+1)\) 都是 \(p\) 单位。最终准确得到唯一分解
\[
\boxed{\quad
f_p=\mathscr D(R_p)+\frac{C_d}{t},\qquad
R_p\in t^{-1}\mathbb Z_p[t^{-2}],\quad
\operatorname{pole}_0(R_p)\le p-4.
\quad}
\tag{10}
\]

为核定最后系数，而非只称其为一个未知常数，注意形式留数的
两次分部积分给
\[
\operatorname{res}K\mathscr D(R)\,dt
=\operatorname{res}R\mathscr D(K)\,dt=0.
\tag{11}
\]
再用 \(K(0)=1\) 与 (7)，得到 (10) 中的系数恰为实际 \(C_d\)。
唯一性也由 (9) 的最高极点项立即得到。

等价地，若
\[
f=\sum_{j=0}^{r}a_jt^{-(2j+1)},\qquad
R=\sum_{j=0}^{r-1}b_jt^{-(2j+1)},
\]
可用以下完全有限的后向递推：
\[
b_{r}=0,\qquad
b_{j-1}=\frac{a_j+(4j+1)^2b_j}{(2j-1)(2j)}
\quad(j=r,r-1,\ldots,1),\qquad C=a_0+b_0.
\tag{12}
\]
其中 \(r=(p-3)/2\)。这给 (10) 的可复算算法，
并明确展示整性来自哪里。

## 3. 精确的权三 Bol 恒等式

这里使用标准 \(\lambda(\tau)\)，不是把
\(\lambda(2\tau)\) 与它混同。令
\[
\Theta(\tau)=\vartheta_3(0,e^{\pi i\tau})^2,\qquad
D_\tau=(2\pi i)^{-1}\frac{d}{d\tau}.
\]
标准 theta 恒等式给
\[
D_\tau t=\frac12\lambda(1-\lambda)\Theta^2
         =\frac{s\Theta^2}{8}.
\tag{13}
\]
其常数可独立由 \(\lambda=16e^{\pi i\tau}+\cdots\) 校准。
\(\Theta\) 作为 \(t\) 的局部函数也满足 \(\mathscr D\Theta=0\)。

写 \(w=\Theta\)，由 (13) 有 \(D_\tau=s w^2\partial_t/8\)。
第一次微分为
\[
D_\tau(R/w)=\frac{s}{8}(wR'-Rw').
\]
再次微分并使用 \((sw')'=w\)，得
\[
\boxed{\quad
D_\tau^2(R/\Theta)
   =\frac{s\Theta^3}{64}\mathscr D(R).
\quad}
\tag{14}
\]
定义
\[
\mathcal F_p=\Theta D_\tau t\,f_p(t),\qquad
\mathcal F_0=\frac{\Theta D_\tau t}{t},\qquad
\mathcal F_1=\frac{\Theta D_\tau t}{t^2}.
\]
由 (10)、(13)、(14)，得到特征零的准确恒等式
\[
\boxed{\quad
\mathcal F_p
=8D_\tau^2(R_p/\Theta)+C_d\,\mathcal F_0.
\quad}
\tag{15}
\]
这里不是将一个 Bol 导数称为非零上同调类。
第一项准确为 exact 部分，非 exact 留数恰为第二项。

### 3.1 固定模曲线与尖点条件

\(\Theta\) 在 \(\Gamma(2)\) 上为权一、字符
\(\chi(\gamma)=\chi_4(d_\gamma)\) 的形式。
可直接在生成元 \(T^2\)、\(\left(\begin{smallmatrix}1&0\\2&1\end{smallmatrix}\right)\)、
\(-I\) 上核对：前两个字符为 \(1\)，最后一个为 \(-1\)。
因此 (15) 是同一固定群和同一字符上的权三恒等式；
\(R_p/\Theta\) 的权为 \(-1\)，字符仍是 \(\chi\)。
也可拉到 \(\Gamma(4)\) 的 fine cover 后取这个字符直和项；
群阶是 \(2\) 的幂，对本篇的 \(p\) 不造成整投影损失。

所有这些 \(\mathcal F\) 只在 \(\lambda=1/2\) 有内点极点，
在三个尖点均消失。证明可直接用 theta 变换：
在 \(\lambda=0,1\) 尖点，\(\Theta D_\tau\lambda\)
有一阶零点，而每个 \(t^{-j}\) 正则；
在 \(\lambda=\infty\) 尖点，取宽度二的参数 \(q_2\)，
\(\Theta\) 的变换为 \(\vartheta_2^2\)，阶为 \(1/2\)，
\(D_\tau\lambda\) 阶为 \(-1\)，而 \(t^{-j}\) 阶为 \(j\)。
总阶 \(j-1/2>0\)。\(R_p/\Theta\) 在尖点也无极点。

同一计算给 \(S_3(\Gamma(2),\chi)=0\)，不必依赖维数表：
若 \(F\) 是全纯尖形式，则
\[
\frac{F}{\Theta D_\tau\lambda}
\]
为 \(\Gamma(2)\) 不变函数，因 \(\lambda\) 是该曲线的坐标，
它是 \(\lambda\) 的有理函数。它在有限平面处处正则，
在 \(\lambda=\infty\) 至少有一阶零点，因此为零。
这里 \(\Theta\) 与 \(D_\tau\lambda\) 在上半平面都没有零点。

## 4. 固定秩二留数格及 Frobenius

Allen–Long–Saad（2025），
[*Atkin and Swinnerton-Dyer congruences for meromorphic modular forms*](https://arxiv.org/pdf/2511.05718)，
§3 Lemma 3.3 的精确序列 (14) 与 Lemma 3.4
（印刷第 15–16 页），把内点极点贡献识别为
\(\operatorname{Sym}^{k-2}H^1_{\rm dR}(E_{\rm pole})(-1)\)；
其 Frobenius 是 \(p\) 倍的纤维 Frobenius。
§3 的 Bol 商比较适用于这里的 \(k=3\)。
本篇用 §3.1 的直接证明消去全纯尖形式部分。

因此固定 \(\lambda=1/2\) 的权三亚纯 Bol 商是秩二，
留数给出其与 \(H^1_{\rm dR}(E_{1/2})(-1)\) 的同构。
可在几何规范中取
\[
\mathfrak c_0=[\,\omega\,dt/t\,],\qquad
\mathfrak c_1=[\,\omega\,dt/t^2\,].
\tag{16}
\]
它们的水平留数分别为 \(\omega_0,\eta_0\)，因为
\((K_0,L_0)=(1,0)\)、\((K_1,L_1)=(0,1)\)。
故两者构成纤维整格的一组基。

由 R68 的准确行约定，
\[
\Phi(\omega^\sigma)=pa_p\eta,\qquad
\Phi(\eta^\sigma)=b_p\omega,\qquad a_pb_p=-1.
\]
留数格上的作用准确为
\[
\boxed{\quad
\Phi(\mathfrak c_0^\sigma)=p^2a_p\mathfrak c_1,\qquad
\Phi(\mathfrak c_1^\sigma)=pb_p\mathfrak c_0,\qquad
\Phi^2=-p^3.
\quad}
\tag{17}
\]
这里写的是几何基 (16)。若改用标量 theta 模形式的 Tate
微分规范，必须同时变换共同基因子与其系数 Frobenius。
例如标准复均匀化满足
\(\omega=\pi_{\mathbb C}\Theta\,dz
       =\Theta(2i)^{-1}\,d(e^{2\pi iz})/e^{2\pi iz}\)；
在惰性处 \(\sigma(i)=-i\)。因此不能无说明地把标量模形式基
当作 (16)，从而漏掉共同因子的共轭。式 (15) 及其 \(C_d\)
在这些共同尺度变化下都保持准确。

由 (8)、(10)，实际类满足
\[
[f_p\omega\,dt]=C_d\mathfrak c_0,\qquad
\frac1p[f_p\omega\,dt]=\Gamma_{i,p}\mathfrak c_0.
\tag{18}
\]
第二式是饱和留数格中的整类；它不宣称
\(f_p/p\) 本身是系数整的亚纯微分。
因此 \(\Gamma_{i,p}\bmod p\ne0\) 正好是这个指定整类模 \(p\)
非零。我们已经得到准确的固定纤维解释，但固定格的非退化性
本身并不强迫这个随 \(p\) 变化的类非零。

## 5. 与真实 Hermite 中央行的一致性

[真实邻点 Hermite 笔记](2026-11-12-hermite-central-trace-and-full-depth-neighbor-jets.md)
使用
\[
m=M/t^4,\quad q=p-3,\qquad
\mathcal R_p=\left[\frac{K^{p+1}}{sJ^{p+2}}\right]_{\le q},
\qquad C_d=[t^q](m\mathcal R_p).
\tag{19}
\]
本篇 (5) 使用 \(K^p\)，因为水平留数时还会乘一次 \(K\)；
所以 (19) 与 (7) 是同一个线性泛函，没有少一个周期因子。
该笔记的 first Hermite 公式模 \(p^2\) 给出 (18) 的同一个
\(\Gamma_{i,p}\)。本篇没有把全部邻点值代替一阶 Hermite 数据。

特别，其反例
\(\Delta M=t^d\mathscr P_p(t)\) 在全部真实邻点取值为零，
却改变 \(\Gamma_{i,p}\) 一个单位，仍然适用。
固定留数解释并未免除所需的一阶导数及迹对偶格成本。

## 6. 尚未支付的实际 Hecke 比较

低 level 的 \(\mathcal F_p\) 使用实际 \(M\) 的有限原点 jet，
所以它完整保留了指定中央值。但是“取指定分支的有限主部”
不是一个已经证明与全部 Hecke 对应交换的算子。

真正保留原 level \(68\) 模形式的候选是，先取
\[
S_p(t)=\left[\frac{K^p}{sJ^{p+2}}\right]_{\le p-3},
\]
再把实际权一 section \(\Theta M\) 乘
\(D_\tau t\,t^{-p-2}S_p(t)\)。
在指定 CM 分支，它与 (5) 的主部相同。但在同一有限 level
覆盖的其他 \(\lambda=1/2\) 标记上，四阶零点不能统一保持。
实际[全 level 留数格笔记](2026-11-12-actual-level-cm-residue-lattice-and-hecke-defect.md)
给出了如下独立证明。若 \(\lambda:X\to X(2)\) 的次数为 \(D\)，
Kodaira–Spencer 与尖点处的 Riemann–Hurwitz 给
\(\deg\omega=D/2\)，而 \(\lambda=1/2\) 的 étale 纤维有 \(D\) 个点。
非零全纯权一 section 因而不可能在整个纤维上消失。
该证明还核定了所有尖点的整性：在每个目标好位，原截面的
约化因指定分支的 \(t^4\) 系数为一而非零。于是同样的次数计算
在特殊纤维给至少 \(D/2\) 个标记满足 \(M_u(0)\bmod p\ne0\)。
所以每个目标 \(p\) 都有实际标记的最高极点确为 \(p+2\)，不能删除。

ALS（2025）§4 Proposition 4.1
（印刷第 17–18 页）证明：极点阶为 \(m+1\) 的主部提升，
相应整上同调余核由 \(m!\) 消灭。
在本篇的 \(p-2\) 阶极点上成本为
\(v_p((p-3)!)=0\)，与 (12) 完全一致；
在上述其他分支上，一般上界为
\(v_p((p+1)!)=1\)，并且对每个目标惰性 \(p\) 都是尖锐的：
选择上面某个 \(M_u(0)\) 为单位的实际标记，所需 \(K\) 的唯一非整项是
\([t^{p+1}]K=\kappa_p/p\)、\(\kappa_p\in\mathbb Z_p^\times\)。
于是该分支水平留数的第一坐标满足
\[
p\,\operatorname{res}_1
\equiv\kappa_p M_u(0)\not\equiv0\pmod p.
\tag{19a}
\]
其余相关 \(K,L,S_p,M_u\) 系数均整，故不能抵消这项。
所选伴随标记可以随 \(p\) 改变，不另加入未确定的有限例外。
该全级笔记还以唯一上升 CM 同源的极点证明：实际权三提升的
几何 Hecke 像确实非零，并写出了保留基底微分和极点核的准确交换子。
本篇没有调用其导言与 Corollary 4.2 之间符号写法不一致的
较强指数，而只使用上述明确的阶乘消灭结论及自己的整消元。

因此下一步真正需要的是：
对原 level \(68\) 的全部 CM 标记和全部同源分支，
证明实际 Hecke/除法单位关系如何作用于这个主部的
Bol 留数类，以及是否约束 \(\Gamma_{i,p}\)。
原权一 \(T_p=0\) 与 (17) 各自成立，仍不能直接合并成
\(\Gamma_{i,p}\ne0\)。

## 7. 更深中央权：准确同一留数线与可见阶乘成本

对每个 \(m\equiv0\pmod4\)、\(m\ge4\)，可同样定义
\[
f_m=t^{-m-1}
\left[\frac{MK^{m-1}}{sJ^{m+1}}\right]_{\le m}.
\tag{20}
\]
它是负奇 Laurent 多项式，最高极点 \(m-3\)。
特征零中相同消元准确给
\[
f_m=\mathscr D(R_m)+C_m/t,\qquad
\operatorname{pole}R_m\le m-5.
\tag{21}
\]
所以所有中央权都落到同一个固定几何线
\(\mathbb Q_p\mathfrak c_0\)。这是精确比较，不是
把一个非零有理标量自动称为非零的 \(p\)-adic 中心导数。

若 \(f_m\) 的各系数先为 \(p\)-整，则 (12) 的全套除数之积是
\[
\prod_{\substack{1\le j\le m-5\\j\ {\rm odd}}}j(j+1)
=(m-4)!.
\tag{22}
\]
因而 \((m-4)!\) 清掉该消元的全部可能分母。
这只是明确上界；它不假设实际分子没有额外约消。
对更深权，输入 \(f_m\) 的周期 jet 本身也可能有分母，
必须另外计入，不能把 (22) 当作完整输入格的唯一成本。

特别 \(m=(p+1)p^n\)、\(n\ge1\) 时，
\[
v_p((m-4)!)
=p^n+2\frac{p^n-1}{p-1}-n.
\tag{23}
\]
证明是
\(v_p(m!)=p^n+2(p^n-1)/(p-1)\)，而
\(m(m-1)(m-2)(m-3)\) 的 \(p\)-赋值准确为 \(n\)。
完整半因子测试使用 \(p^{p^n}C_m\)；
因此即使先假设输入整，单由一般阶乘界也还留下
\(2(p^n-1)/(p-1)-n\) 的可能成本。
不能仅凭固定留数 Frobenius 的斜率 \(3/2\)
便把完整中心消失判据与它相矛盾。

要获得这样的矛盾，仍需一个实际跨 \(m\) 的式子，
把 (21) 的这些不同主部类识别为同一个固定类的 Frobenius
迭代，并完整保留两变量 theta 的公共参考项与非齐次修正。
本篇尚未证明这个迭代等式。

## 8. 可复算校验及来源

[脚本](../scripts/check-central-pf-bol-residue.py)
从 R57 的实际整数多项式流独立生成 \(M,K,L\)，
对默认 \(p=7,11,19\) 逐项验证 (5)、(10)、(12)，并将最后
留数与 (4) 的准确有理数比较；它还核验所有消元系数 \(p\)-整。
这些计算用于校准，普遍证明是上文的有限主部消元。

外部输入只用 ALS（2025）§3–4 的 Bol/留数比较及阶乘成本；
本篇所有周期、字符、尺度和首层整性均在正文展开。
标准 theta 定义与变换亦可核对
[DLMF（2026 年查阅）§20.7(viii)](https://dlmf.nist.gov/20.7.viii)
及 [§23.15](https://dlmf.nist.gov/23.15)。
没有引入尚未计算的坏素数集合。
