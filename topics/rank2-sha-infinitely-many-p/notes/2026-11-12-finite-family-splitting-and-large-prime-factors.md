# 有限辅助域同时分裂的补集删除与大素因子

日期：2026-11-12。**本篇的筛法结论已证明。** 它只选择素数，
不独自证明任一完整 Heegner 迹非零或二次增广原始性。
与 R126 的区别是：不指定单个正密度分裂类，而删除一个可以
准确控制密度的很小补集。全部模数先固定，再令 $x\to\infty$。

## 1. 准确的补集上界

设 $B$ 为固定偶正整数，$D\mid B$，
$\mathcal S\subset(\mathbb Z/D\mathbb Z)^\times$，记
$$
 \epsilon=\frac{|\mathcal S|}{\varphi(D)},\qquad
 \frac12<\vartheta<1.
$$
定义
$$
 \begin{split}
 \mathcal N_{B,\mathcal S}(x)=\#\{\ell\le x:\;&\ell\text{ 素},\quad
 \ell\equiv-1\pmod B,\\
 &\exists\ p>x^\vartheta\text{ 素},\quad
 p\mid\ell+1,\quad p\bmod D\in\mathcal S\}.
 \end{split}
\tag{1}
$$
则
$$
 \boxed{\quad
 \mathcal N_{B,\mathcal S}(x)
 \le\left(64\epsilon\frac{1-\vartheta}{\vartheta^2}
                  +o_{B,D}(1)\right)
                  \frac{x}{\varphi(B)\log x}.
 \quad}
\tag{2}
$$
若 $\mathcal S$ 为空，左侧为零。下面假设它非空。
常数 $64$ 对 $B,D,\mathcal S$ 一致；趋于零的误差和起始阈值
允许依赖这些固定数据。这一点使随后选择十六个固定域合法。

## 2. 保留全部局部因子的二维 Selberg 上界

令 $u$ 为偶数，$D\mid u$，$(a,D)=1$。在长度 $N$ 的整数区间
筛两个线性式
$$
                 L_1(t)=a+Dt,\qquad L_2(t)=u(a+Dt)-1.
\tag{3}
$$
对素数 $q$，乘积 $L_1L_2$ 的模 $q$ 根数为
$$
 \rho(q)=
 \begin{cases}
 0,&q\mid D,\\
 1,&q\mid u,\ q\nmid D,\\
 2,&q\nmid uD.
 \end{cases}
\tag{4}
$$
最后一种情形的两根相异，因为两式的公共根会使
$uL_1-L_2=1$ 为零。由于 $u$ 偶，$\rho(2)<2$。
根数与 $a$ 无关，且对每个平方自由 $d$，中国剩余定理给
$$
  \#\{t\text{ 在该区间}:d\mid L_1(t)L_2(t)\}
       =N\frac{\rho(d)}d+O(\rho(d)),
\tag{5}
$$
误差的绝对常数不依赖任何线性式系数。

置
$$
 g(q)=\frac{\rho(q)}q,\qquad
 h(q)=\frac{g(q)}{1-g(q)},\qquad
 G(R)=\sum_{d\le R}\mu^2(d)h(d).
$$
只在 $\rho(q)>0$ 的素数上筛。Selberg 的有限二次型优化给
支撑在 $d\le R$ 的权，首项 $\lambda_1=1$，以及
$$
 S(N,R)\le\frac N{G(R)}+
 O\left(\sum_{d,e\le R}|\lambda_d\lambda_e|
                                      \rho([d,e])\right).
\tag{6}
$$
这里 $S(N,R)$ 是两个线性式均不被任何 $q\le R$ 整除的项数。
其准确最优权满足
$$
 |\lambda_d|
 \le\prod_{q\mid d}(1-g(q))^{-1}
 \le 2\prod_{3\le q\le R}(1-2/q)^{-1}
 \ll (\log R)^2.
\tag{7}
$$
例如可直接使用
$\lambda_d=\mu(d)G_d(R/d)/(G(R)\prod_{q\mid d}(1-g(q)))$，
其中 $G_d$ 的和只取与 $d$ 互素的指标；$G_d\le G$。
所有常数均绝对。由
$\rho([d,e])\le2^{\omega(d)}2^{\omega(e)}$ 及
$\sum_{d\le R}2^{\omega(d)}\le\sum_{d\le R}\tau(d)\ll R\log R$，
(6) 的误差为
$$
                         O(R^2(\log R)^6).
\tag{8}
$$
因此该步骤对随 $x$ 增长的 $u$ 仍然一致，并非固定两个线性式
后才得到的含未知 $u$ 常数的渐近式。

### 2.1 一个足够小的绝对主常数

取 $R=N^{2/5}$、$z=R^{1/3}$。把所有素因子不超过 $z$ 的
平方自由整数按权 $h(d)$ 归一为概率分布。其总质量和
$\log d$ 的均值分别为
$$
 W(z)=\prod_{q\le z}(1+h(q))
       =\prod_{q\le z}(1-\rho(q)/q)^{-1},
$$
$$
 \mathbb E(\log d)=\sum_{q\le z}\frac{\rho(q)\log q}{q}
                    \le2\log z+O(1).
$$
Markov 不等式于是给
$$
        G(R)\ge\left(\frac13-o(1)\right)W(z).
\tag{9}
$$
误差一致于 $u,D$，因为只用了 $\rho(q)\le2$。

定义准确奇异级数
$$
 \mathfrak S(u;D)
  =\prod_q\frac{1-\rho(q)/q}{(1-1/q)^2}.
$$
在 $q>z$ 的尾乘积中，普通因子是
$1-(q-1)^{-2}$；$q\mid uD$ 的例外因子大于等于一。
所以全尾乘积至少为 $1-O(1/z)$，一致于 $u,D$。
Mertens 乘积式和 (9) 给
$$
 \frac1{G(R)}
 \le(27e^{-2\gamma}+o(1))
                      \frac{\mathfrak S(u;D)}{(\log R)^2}.
\tag{10}
$$
又有 $\gamma>1/2$、$e>27/10$，故
$$
 \frac{27e^{-2\gamma}}{(2/5)^2}
       <\frac{675}{4e}<\frac{125}{2}=62.5.
$$
(8) 为 $O(N^{4/5}(\log N)^6)$；奇异级数有绝对正常数下界，
所以将它吸收进主项后，对充分大且一致的 $N$ 有
$$
          \boxed{\ S(N,N^{2/5})
              \le64\,\mathfrak S(u;D)\frac N{(\log N)^2}.\ }
\tag{11}
$$
这里只需要一个宽松常数，不使用最优 twin-prime 常数。

### 2.2 $D$ 的密度和 $B$ 的奇异因子准确抵消

记通常的两线性式奇异级数
$$
 \mathfrak S(u)=2C_2
       \prod_{\substack{q\mid u\\q>2}}\frac{q-1}{q-2},
 \qquad C_2=\prod_{q>2}\left(1-\frac1{(q-1)^2}\right).
$$
从 (4) 逐素数比较，包含 $q=2$ 在内，有
$$
                     \mathfrak S(u;D)
                       =\mathfrak S(u)\frac D{\varphi(D)}.
\tag{12}
$$
若 $p=a+Dt\le Y$，区间长度是 $N=Y/D+O(1)$。
对 $|\mathcal S|$ 个剩余类求和，(12) 中的因子恰给
$|\mathcal S|D/(D\varphi(D))=\epsilon$；没有多付一个
$D/\varphi(D)$。

还需保留 $u=Bm$ 的平均。对 $B$ 偶，平方自由除数展开给
$$
 \mathfrak S(Bm)=\mathfrak S(B)
 \sum_{\substack{d\mid m\\(d,B)=1}}
       \frac{\mu^2(d)}{\prod_{q\mid d}(q-2)}.
$$
因而对 $M\ge1$，
$$
 \begin{split}
 \sum_{m\le M}\frac{\mathfrak S(Bm)}m
 &\le\mathfrak S(B)(\log M+1)
       \prod_{q\nmid B}\left(1+\frac1{q(q-2)}\right)\\
 &=\frac B{\varphi(B)}(\log M+1).
 \end{split}
\tag{13}
$$
最后的等式由 $C_2$ 的 Euler 因子逐项相消得到。
这里 $(d,B)=1$ 已排除素数二，故没有 $q-2=0$ 的项。
这是所需对固定模数一致的归一化，不能以一个任意依赖 $B$
的上界替代。

## 3. 证明补集上界

对 (1) 的每一项，$p>x^\vartheta$ 且 $\vartheta>1/2$，
所以这种素因子至多一个。对充分大 $x$，$p\nmid B$，从
$B\mid\ell+1$ 得
$$
 u=(\ell+1)/p=Bm,\qquad
 m\le M_x:=\frac{x+1}{Bx^\vartheta}.
$$
固定 $m$，取 $Y=(x+1)/(Bm)$。上述整数区间长度满足
$$
          N=Y/D+O(1)\ge x^\vartheta/D+O(1),
          \log N\ge\vartheta\log x-O_D(1).
$$
目标项的两素数 $p$ 与 $up-1$ 均大于筛界 $N^{2/5}$，
因为它们至少为 $x^\vartheta-1$，而
$N^{2/5}\le(x+1)^{2/5}$。所以均被 (11) 计入。
用 (12)、(13) 后，
$$
 \begin{split}
 \mathcal N_{B,\mathcal S}(x)
 &\le(64+o_{B,D}(1))
       \frac{\epsilon(x+1)}{B\vartheta^2(\log x)^2}
              \sum_{m\le M_x}\frac{\mathfrak S(Bm)}m\\
 &\le\left(64\epsilon\frac{1-\vartheta}{\vartheta^2}
                  +o_{B,D}(1)\right)
                      \frac{x}{\varphi(B)\log x}.
 \end{split}
$$
这证明 (2)。区间长度中的 $O(1)$、固定 $D$ 的对数平移和
有限起始素数均被一致误差吸收；没有将 $\log(x/p)$ 在端点
附近粗暴替换为 $\log x$。

## 4. 十六个独立二次角色足够

现在固定
$$
                       \vartheta=667/1000.
$$
设 $F_1,\ldots,F_{16}$ 是十六个虚二次域，其二次角色
在 $\mathbb Q^\times/\mathbb Q^{\times2}$ 中独立。
令 $D$ 为其导子的最小公倍数，$2D\mid B$。
中国剩余定理与角色独立性给
$$
 \mathcal S=\{a\in(\mathbb Z/D\mathbb Z)^\times:
                         \chi_{F_j}(a)=-1\text{ 对所有 }j\},
 \qquad\frac{|\mathcal S|}{\varphi(D)}=2^{-16}.
\tag{14}
$$
因为各域均为虚二次，$\chi_{F_j}(-1)=-1$，故
$\ell\equiv-1\pmod B$ 保证 $\ell$ 在所有这些域惰性。

R126 已保留固定进程主项的 Fouvry--Tenenbaum 勘误，给
$$
 \#\{\ell\le x:\ell\equiv-1\pmod B,\ \ell\text{ 素},
                     P^+(\ell+1)>x^\vartheta\}
 \ge\left(\frac12-I- o_B(1)\right)
                          \frac{x}{\varphi(B)\log x},
\tag{15}
$$
其中 $I<0.498641$，因此 $1/2-I>0.001359$。
另一方面，(2)、(14) 的坏类系数为
$$
 64\cdot2^{-16}\frac{1-\vartheta}{\vartheta^2}
       =\frac{333000}{455566336}<\frac3{4000}=0.00075.
\tag{16}
$$
于是 (15) 删去全部“在十六域都惰性”的大素因子后，
仍至少有
$$
                 \frac1{2000}\frac{x}{\varphi(B)\log x}
\tag{17}
$$
个辅助素数（对充分大 $x$）。可以继续删除任意
$o_B(x/\log x)$ 个坏辅助素数，结论仍为
$\gg_B x/\log x$。例如 R138 的非 CM 异常删除就在此范围。

每个留下的输入满足
$$
 \begin{gathered}
 p=P^+(\ell+1)>x^{667/1000},\qquad v_p(\ell+1)=1,\\
 u=(\ell+1)/p\ll p^{333/667},\qquad u^2=o(p),\\
 p\text{ 至少在一个固定 }F_j\text{ 分裂}.
 \end{gathered}
\tag{18}
$$
这些 $p$ 无界，且有限鸽巢原理给某个**固定**的 $F_j$，
使 (18) 中该分裂条件发生于无穷多个不同的 $p$。
没有对两个任意无穷集合求交；真正支付的是 (2) 的坏补集上界。

## 5. 与原课题的边界

本篇不将“十六域的选择”直接当成原完整 Heegner 迹的非零。
若要用于固定 $E389$ 的 $o(p)$ 实际点，必须另对每个域核清：

1. $389$ 分裂、完整 Hilbert 类群和、原 $C_p$ 商及整数规范；
2. 固定辅助进制下的真实总 jet 非零进程，而非单中心的 jet；
3. 同一个 $u$ 上 $\log|J_u|\ll u\log u$ 的完整整数证书；
4. 两步判据中全部局部条件。

有限域集允许把这些固定整数进程合入同一个 $B$，但只有在
这些输入分别确实已证明时才可这样使用。即使得到小高度且
源普通的实际点，原 $a\le1$ 或指定 CM 两矩非零仍须另证。

## 一手来源及证明归属

- Selberg 有限二次型优化可见 K. Ford，*Sieve methods lecture
  notes, Spring 2023*，Theorem 4.1 和该节的最优权公式，
  [作者全文](https://ford126.web.illinois.edu/sieve2023.pdf)。
  本篇 (4)--(13) 给所需全部一致性、绝对常数与局部因子的独立推导。
- E. Fouvry，Invent. Math. **79** (1985), 383--407，§VI 及
  固定附加同余说明；Fouvry--Tenenbaum，Proc. LMS **72**
  (1996), 481--514 的勘误。准确主项和纯有理积分证书已完整
  保存于 R126 及其笔记。
- (14)--(18) 是将这个实际补集上界与已核固定进程下界合并，
  不是从文献中引用一个带未核局部限制的新大素因子定理。
