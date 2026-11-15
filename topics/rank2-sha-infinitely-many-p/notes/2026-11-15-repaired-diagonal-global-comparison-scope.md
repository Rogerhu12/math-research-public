# 修复后低权对角类的全局高度与指定 AJ：引用范围

状态：**来源范围核查；未证明新全局非零。** 2026-11-15。
本注对应 [R830](../results/R830-distinct-degeneracy-test-vectors-and-fourth-slot.md) 的固定不同退化向量。
不增加数值计算，不把未核实稿件用作主目标证明输入。

## 1. 本课题已经支付的输入

[R826](../results/R826-fixed-low-weight-cm-triple-and-fourth-de-rham-slot.md) 的三组固定
$(f,g_j,h_j)$ 满足 $N_f=10404$、$N_g=N_h=2601$，对应表示在有限位恰于
$2,3,17$ 分歧。R818及R826的完整因子分解给三重积的中心解析秩1。
R830已把第三个old输入改为 $q_4^*h$，并证明全部有限位的指定三线性测试非零。

这三件事不因换 $q_4$ 而使局部表示未分歧：换的是同一表示中的向量。
R829原同 $q_0$ 的类已为零；以下只讨论R830新类。

## 2. 已亲读的 YZZ 版本保留分歧补项

X. Yuan、S.-W. Zhang、W. Zhang，*Triple product L-series and Gross–Kudla–Schoen cycles*，
作者所载 2023-11-14 版本：
[全文](https://web.math.princeton.edu/~shouwu/publications/triple2023.pdf)，
§1.3，Conjecture 1.3.1、Proposition 1.3.2、Theorem 1.3.3（正文第7–8页）。

该版本将高度写成 $\mathscr L(\pi)\alpha(v,\widetilde v)$；
Theorem 1.3.3 对分歧表示保留
$$
\mathscr L(\pi)=
 \frac{16\zeta_F(2)^2}{L(1,\pi_L,\mathrm{ad})}
 L'(1/2,\pi_L)+\sum_{\ell\in P}c_\ell\log\ell,
 \qquad c_\ell\in\overline{\mathbf Q}.
\tag{1}
$$
这里 $P$ 是位于表示分歧位下方的有理素数集。
本课题的 $P=\{2,3,17\}$，所以不能直接删去这三项。
该版本明确在未分歧情形得到无补项的猜想公式。

因此，仅将R830的非零局部测试和R818的复导数非零代入(1)，
还没有排除右端补项相消。
这不是断言原稿结论错误，也不是断言不存在更强的其他定理；
这里只记录所检定理未支付本题的这一接口。
按本课题README，尚未被公认的论证若要实际使用，仍需本仓库完整证明。

## 3. 另一个已发表惰性定理也保留指定非零输入

L. Marannino，*Diagonal cycles and anticyclotomic twists of modular forms at inert primes*，
Research in the Mathematical Sciences 13 (2026), article 70，2026-08-17发表，
[期刊全文](https://doi.org/10.1007/s40687-026-00651-w)，
§1、Assumption 1.1、Theorem 1.2。

该定理假设第一模形式非CM、大像、平方自由level，且其level与CM判别式互素；
结论由一个指定反圆分 $p$-adic $L$ 值非零推出Selmer维数1。
它没有给出该指定值非零。
当前 $f$ 是CM、level $10404$ 非平方自由，且与判别式3不互素，
故不能直接套用。改变ordinary素数集合也不改变这些固定障碍。

## 4. 继续所需的是哪条实际等式

R830已付的精确式仍是
$$
\operatorname{AJ}_p(\Delta_{04})(\omega_f\omega_{g,0}\omega_{h,4})
 =
 \frac{\left\langle\omega_f,
 [\,\{4G_g(Q)h(Q^4)-\bar\pi G_h(Q^4)g(Q^p)\}\,dQ/Q\,]\right\rangle}
 {1+\bar\pi/\pi^2}.
\tag{2}
$$
分母和所有有限局部因子非零，没有证明(2)的分子非零。
本课题还须证明新类的原 $\lambda_j$ 投影与
[R814](../results/R814-common-fixed-good-pair-and-three-original-aj-squares.md)
指定类的真实全局比较，或直接控制(2)在无穷多个目标 $p$ 的值。

即使另行证明某个复高度或Chow类非零，也仍须支付到这里这个指定
$p$-adic局部AJ泛函的桥；R817在7993的非零不自动传播到其他素数。
本注没有关闭原跨 $p$ 非零、三原值线性行或全Sha主目标。

## 5. 分歧补项的确切 Fourier 定义

本节补核同一YZZ版本的§5.5（正文第69–71页）。
记 $\mathcal E(g,\Phi)$ 为 $E'(g,0,\Phi)$ 的全纯投影，
$S$ 为 $\Phi_v$ 非球向量的有限位集；星号表示非奇异Fourier部分。该节给
$$
\Theta+2\mathcal E
 =\Theta_{\mathrm{sing}}+
   \sum_{v\in S}\Delta_v,\qquad
\Delta_v:=\Theta_v+2\mathcal E_v.
\tag{3}
$$
Conjecture 5.5.1断言每个 $\Delta_v$ 是某Eisenstein级数的非奇异部分。
**这仍是该版本的猜想，不是其坏位证明。**

实际已证的Proposition 5.5.2只给代数模形式 $f_\ell$，满足
$$
\Theta+2\mathcal E=\sum_{\ell\in P'}f_\ell\log\ell,\qquad
f_\ell^*=\frac{1}{\log\ell}\sum_{v\mid\ell}\Delta_v .
\tag{4}
$$
这里 $P'$ 暂含为确保局部测试非零而引入的两个辅助位；
结尾的辅助位独立性把最终补项支持缩回 $P$。

在Theorem 1.3.3的证明中，取实际 $\varphi\in\sigma$ 后，等式(4)成为
$$
(\Theta,\varphi)+(2\mathcal E,\varphi)
 =\sum_{\ell\in P'}(f_\ell,\varphi)\log\ell .
\tag{5}
$$
其中 $(f_\ell,\varphi)$ 是 $f_\ell$ 的真正 $\sigma$ 尖点投影。
若写 $(f_\ell,\varphi)=\Omega(\sigma)d_\ell$，
其证明中的中间归一系数为
$$
c_\ell^{\mathrm{proof}}
 =-\frac{8d_\ell}{\alpha(f,\widetilde f)}.
\tag{6}
$$
这不是把(1)的所有全局周期重新吸入后的同名系数；(6)仅保该证明所用规范。
因此原补项的消失需要控制这些尖点投影。
所引等式没有把它们写成
$L(1/2,\pi_L)$ 乘一个局部导数；中心根数为负不能单凭该形式理由删项。
若另能证明(3)各局部差的Eisenstein性质，则其尖点投影才随之为零。

## 6. 纯 $\lambda$ 与17处Artin投影不能独自删掉高度误差

[R832](../results/R832-original-triple-chow-purity-and-rank-zero-contractions.md)
已证明修复后的唯一端点类在Chow群中属于原 $\lambda_j$ 分量。
这条来源纯性完整保留，但高度配对有两个输入，第二输入在对偶分量。

具体地，令 $I$ 为17处有限Artin商，$\vartheta$ 为原非平凡有限角色。
在系数域上若 $Z\in M_\vartheta$、$\widetilde Z\in M_{\vartheta^{-1}}$，
任何 $I$ 不变双线性配对 $B$ 都满足
$$
B(\sigma Z,\sigma\widetilde Z)
 =\vartheta(\sigma)\vartheta(\sigma)^{-1}
   B(Z,\widetilde Z)
 =B(Z,\widetilde Z).
\tag{7}
$$
等价地，真正的对偶恒等式是
$$
B(e_\vartheta Z,\widetilde Z)
 =B(Z,e_{\vartheta^{-1}}\widetilde Z),
\tag{8}
$$
而非把第二输入也替成平凡分量。
所以 $\lambda_j\otimes\lambda_j^\vee$ 中原17字符相消；
非平凡 $\vartheta$ 不强迫高度或(5)的补项为零。
这是双线性等变性的直接计算，不使用任何未证的局部高度消失。

同样，某个 $\ell$-adic实现满足 $V^{I_{17}}=0$，
本身没有给(3)的垂直相交核或(5)的尖点投影消失。
要利用原CM对应消项，仍须在 $\Delta_v$ 的实际几何/Fourier定义上计算。
本注没有把这个待算对应替换成实现的维数论证。

## 7. 新 arithmetic Siegel–Weil 公式的实际层范围

下表只记录已亲读正文的范围，不否定更一般公式的可能性。

| 来源 | 已读定理或定义 | 与本题坏位的关系 |
|---|---|---|
| R. Chen–B. Zhu，*Arithmetic Siegel–Weil formula on the product of modular curves*，[arXiv:2610.20575](https://arxiv.org/pdf/2610.20575)，§8.4，第35–36页 | 标准层 $K^\circ=H(\widehat{\mathbf Z})$；一般 $K\subset K^\circ$、在 $S$ 外标准时，$\mathcal M_K$ 定义于 $\mathbf Z[1/S]$，遗忘映射在那里有限étale | 在 $2,3,17$ 增加本题层结构会反演这些位；该处构造本身不计算其垂直误差 |
| Q. He–B. Zhu，*Intersections of Hecke correspondences on modular curves*，[arXiv:2502.19600](https://arxiv.org/pdf/2502.19600)，§1.1、Theorem 1.2.2 | 全局 $N$ 为奇数且平方自由；局部为 $\Gamma_0(\ell)$ 的 $H_0(\ell)$ 模型及其对偶密度 | 不覆盖原 $N=10404=2^2\,3^2\,17^2$ 的指定向量与积分模型 |
| Q. He–Z. Zhang–B. Zhu，*Weighted special cycles on Rapoport–Zink spaces with almost self-dual level*，[作者全文](https://bqzhu14.github.io/assets/pdf/WeightedKR.pdf)、[arXiv:2504.07768](https://arxiv.org/pdf/2504.07768)，§1.1–1.2 | 主范围 $\ell>3$，特殊极大parahoric、$L^\vee/L\simeq\mathbf F_\ell$；权值是该模型的向量值特殊循环 | 不能仅因“weighted”字样就把本题平方导子depth-zero向量搬到该模型 |

这些文献未在上述被核条款中给出原 $\Delta_2,\Delta_3,\Delta_{17}$ 的指定尖点投影。
原 $(q,q^4)$ 端点、原有限测试及(2)第四槽继续保持；
(3)–(8)也没有给R814指定类的跨 $p$ AJ非零。
