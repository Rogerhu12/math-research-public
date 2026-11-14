# R158. 实际混合列的普通饱和 jet 界

**状态：已证明。** 结论针对 R155 的同一个原普通系数源格，
尚未包括惰性位，也不单独证明中央导数非零。

固定 $w=z^4$、$A_2=A(2z)/16$、$B=R(x^2)A_2$，源列为
$w^aA_2^bB^c$、$a+b+c\le D$。令 $r_j$ 为 $w^j$ 系数行，
$\varphi_D^k$ 为 $r_k$ 在前 $k$ 行真正饱和核上的评价。
对普通 $p\equiv1\pmod4$、$p\ge13$、$p\ne17$，置
$K=4\min(D,k)$。则

$$
\log\|\varphi_D^k\|_p\le\Gamma_p(D,k)\log p,
$$

$$
\Gamma_p(D,k)=
\max_{\substack{0\le j\le K\\4\mid j}}
\left\{\sum_{h\ge1}\min\!\left(\left\lfloor\frac{4k}{p^h}\right\rfloor,j\right)
       -v_p(j!)\right\}.
$$

证明使用同一个 falling-factorial 多项式
$\mathcal F_{4k}(x)=\prod_{v=0}^{4k-1}(x-v)$，不是对每一列分别选行。
每个自然参数幂 $w^a$ 对应整 Amice 测度的 $4a$ 阶分布导数；
$\mathcal F_n^{(j)}$ 的整值下界为

$$
v_p(j!)+\sum_{h\ge1}\max(\lfloor n/p^h\rfloor-j,0).
$$

由实际矩规范 $\nu_P(x^{4j})=\Omega_p^{4j}(4j)!r_j(P)$，积分得到
对全部混合列共用的低阶行关系。最高阶乘的全部 $p$ 成本保留在
$\Gamma_p$ 中；限制到饱和核后，低阶行准确为零。

对所有 $1\le D\le k$，全普通素数统一给

$$
\boxed{\quad
\sum_{\substack{p\equiv1\ (4)\\p\notin S}}
 \log\|\varphi_D^k\|_p
 \le 2k\log(4D)+O(k).
\quad}
$$

常数与 $D,k$ 无关。小素数阈值是 $4k/(4D)=k/D$，其总成本为
$O(k)$；主项来自此阈值以上的固定模四 Mertens 和。
该式是次数敏感界，不能仅代入 $D\asymp k^{1/r}$ 就宣布完整
arithmeticity。R159 另以全部真实跳跃的乘积公式处理这一点。

完整证明还给出单一 Taylor 行逼近全部列的 $p\Lambda_p$：取
$s-\lfloor\log_p s\rfloor\ge N+4D$，显式 Hermite 多项式在
整个 $\mathbb Z_p$ 上同时逼近完整单位对数核及前 $4D$ 阶导数，
最高只需 $w$ 阶 $((p-1)/4)(2s-1)$。已知两条原中央行消失
不会自动使该行在其余混合列上消失。

同文证明实际 $(w,A_2,B)$ 的 Zariski 闭包为三维，原点为
$\mathbb Q$ 点，复增长为有限型阶 $1/2$。普通估计、维数和
所有规范都对应这一真实源，没有暗换成 Hurwitz 格或另加坐标。

**实际平面加强。** 若直接采用固定平面 $(A_2,B)$，源为
$P(A_2,B)$ 而没有自由 $w$ 列，分布阶为零。相同 falling-factorial 行
使最高阶乘完全抵消，故所有上述普通位都有
$\|\varphi_{D,2}^k\|_p\le1$，全普通成本非正。
该平面仍代数稠密、原点有理且复阶为有限型 $1/2$。
改用 $V$ 只作输出形式参数时，原整源准确为
$F(V)^jV^c$、$0\le c\le j\le D$；没有加入自由 $V$ 列。
R159 的惰性剩余严格门槛因此是 $a_I+2b_I<2$，该界仍未证明。

详见[完整证明](../notes/2026-11-12-ordinary-falling-factorial-saturated-jets.md)。
依赖 R117、R155 的实际 theta/Amice 比较及 R151 的饱和前缀判据。
