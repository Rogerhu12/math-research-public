# 实 $q$ 分支的对角尖点、精确尾级数与完整覆盖核验

日期：2026-11-12；会话：serre-uniformity-resume2。

**范围：** 独立核验 R101 后续紧区间计算所需的数学公式及当前搜索器的证明接口。本笔记不引用 BBM 的整点分类结论，也不把一个尖点或一部分相位的计算当成全部整点覆盖。对角矩阵、系数 $-4/N$、相位折半、实 $j$ 三段、自然区间叶判据和尾界均在下面推导。

审读的临时实现为根会话的 `/tmp/serre-unit-curve.py` 与 `/tmp/serre-unit-cover.py`；正式证书必须另存可复核版本，临时路径本身不是结果证书。

## 1. 对角尖点代表确实覆盖所有尖点

记 $d=(p-1)/2$，采用 R101 的本原根 $g$、非平方 $\xi$，及行向量轨道
$$
\mathcal O_k=\{(x_0,y_0)\ne(0,0):
\xi x_0^2-y_0^2=\pm g^k\},\qquad 0\le k<d.
$$
尖点由列向量的
$$u^2-\xi v^2\pmod{\{\pm1\}}$$
标记，因此 $c=1,\ldots,d$ 给全部尖点。

固定 $c$，选 $a,b\in\mathbb F_p$ 满足
$$a^2-\xi b^2=c^{-1}.$$
有限域范数映射满射，故这样的 $a,b$ 存在。置
$$
\boxed{\sigma_c=
\begin{pmatrix}
ca&\xi b\\cb&a
\end{pmatrix}.}                                           \tag{1.1}
$$
其行列式是 $c(a^2-\xi b^2)=1$；第一列的尖点不变量为 $c$。它可以提升到 $\operatorname{SL}_2(\mathbb Z)$，绝对值级数只依赖模 $p$ 的轨道数据。

若 $(x,y)=(x_0,y_0)\sigma_c$，则
$$
(x_0,y_0)=(ax-cby,\ -\xi bx+cay),
$$
所以交叉项严格消失：
$$
\boxed{
\xi x_0^2-y_0^2=\frac{\xi}{c}x^2-cy^2.
}                                                        \tag{1.2}
$$
因此
$$
\boxed{\mathcal O_k\sigma_c=
\{(x,y)\ne0:(\xi/c)x^2-cy^2=\pm g^k\}.}                  \tag{1.3}
$$
此集合分别稳定于 $x\mapsto-x$ 和 $y\mapsto-y$。对固定 $x$，两个二次方程的 $y^2$ 系数为非零的 $-c$，故至多有四个 $y$。

同一标号的旧 R101 尖点代表与 (1.1) 相差左乘 $G\cap\operatorname{SL}_2$ 和右乘某个 $T^r$。左乘保持每个 $\mathcal O_k$，右乘 $T^r$ 保持目标行向量第一坐标，并在第一坐标为零时保持第二坐标。因此新代表的 Bernoulli 斜率 $V_k$ 与首项常数 $W_k$ 正是 R101 已保存的值。实现中的有限精确断言核对这两个相等，具有正确数学含义。

每个尖点宽度为 $p$。全部标准域代表可取
$$\sigma_cT^r,\qquad 1\le c\le d,\quad0\le r<p.$$
总数 $pd=p(p-1)/2$，等于
$$[\operatorname{SL}_2(\mathbb F_p):
G\cap\operatorname{SL}_2(\mathbb F_p)],$$
故这里没有少取某类域分支。

## 2. 实 $j$ 的三个区域及精确下端点

对标准基本域 $\mathcal F$，$j(-\bar\tau)=\overline{j(\tau)}$，且 $j$ 在模群商上给一一参数。基本域的边界识别因而给
$$
\begin{array}{c|c|c}
j\text{ 范围}&\tau\text{ 可选形式}&q=e^{2\pi i\tau}\\ \hline
[1728,+\infty)&iy,\ y\ge1&e^{-s},\ s=2\pi y\ge2\pi\\
(-\infty,0]&1/2+iy,\ y\ge\sqrt3/2&-e^{-s},\ s\ge\pi\sqrt3\\
[0,1728]&|\tau|=1&\text{通常非实}
\end{array}                                               \tag{2.1}
$$
端点为 $j(i)=1728$、$j(e^{\pi i/3})=0$。在虚轴或竖直边上，$j$ 连续实值且在商上单射；结合尖点处 $q^{-1}$ 的符号即得到表中完整范围。单位圆边由 $\tau\sim-1/\tau=-\bar\tau$ 给实值，并连接上述两个端点。

因此实 $q$ 计算**本身不覆盖**整数 $1,\ldots,1727$。本项目可接入 R101 §10 的完整独立点数证书来排除此段；$j=0,1728$ 必须保留为 CM 端点，不能丢掉闭区间端点。

在尖点分支 $\sigma_cT^r$ 上，把 $r$ 合进变量，写
$$
z=r+\varepsilon/2+i\,s/(2\pi),\quad
\varepsilon\in\{0,1\},\quad h=2r+\varepsilon.
$$
则
$$
e^{2\pi iz}=(-1)^h e^{-s},\qquad
e^{2\pi iz/p}=e^{\pi ih/p}e^{-s/p}.                      \tag{2.2}
$$
这里 $0\le r<p$、$\varepsilon=0,1$ 恰给全部
$$h=0,1,\ldots,2p-1.$$
正 $q$ 对应偶 $h$ 和 $s\ge2\pi$，负 $q$ 对应奇 $h$ 和 $s\ge\pi\sqrt3$。

若实际计算把下端点向下取到分母 $2^{64}$ 的有理数，它只多纳入一小段参数，不会漏掉真实点。级数和尾界在这个稍大的区间仍收敛。上端必须接入 R101 每层已认证的全局上界，而非仅某个尖点的经验终止值。

## 3. 从 Siegel 双侧乘积推导系数 $-4/N$

设 $0\le x,y<p$，Siegel 函数的绝对值乘积写为
$$
\begin{aligned}
\log|g_{(x/p,y/p)}(z)|
={}&-\tfrac{s}{2}B_2(x/p)\\
&+\sum_{n\ge0}\log|1-\zeta_p^y e^{2\pi iz(n+x/p)}|\\
&+\sum_{n\ge1}\log|1-\zeta_p^{-y}e^{2\pi iz(n-x/p)}|.
\end{aligned}                                             \tag{3.1}
$$
$x=0,n=0$ 的项是常数 $\log|1-\zeta_p^y|$；它先收入 $W_k$，不放入正幂尾部。变换律或代表改变引起的单位根不影响 (3.1)。

固定轨道 $R_k=\mathcal O_k\sigma_c$。在第二个和中，把
$$(x,y)\longmapsto(-x,-y)\pmod p$$
重新编号；$R_k$ 稳定于此变换。对于 $x>0$，指数 $np-x$ 改写成 $(n-1)p+(p-x)$；对于 $x=0$，指数仍是 $np$，从 $n=1$ 起。于是两个正幂尾部的轨道总和严格相等。

R101 的模单位指数为 $m=2$。所以对
$$\lambda_k(s,h)=\log|U_{\mathcal O_k}(\sigma_c z)|,$$
有
$$
\lambda_k(s,h)=V_ks+W_k+
4\sum_{d_0\ge1}\sum_{y:(d_0\bmod p,y)\in R_k}
\log\left|1-
e^{-sd_0/p}e^{\pi ihd_0/p}e^{2\pi iy/p}\right|.            \tag{3.2}
$$
这个因子四同时来自双侧乘积的二与模单位指数的二，不能再除以二。

对绝对值小于一的复数 $\rho$，
$$\log|1-\rho|=-\sum_{n\ge1}\frac{\operatorname{Re}(\rho^n)}n.$$
在任意 $s\ge s_0>0$ 上绝对一致收敛，可以交换有限轨道和与双重级数。令 $N=d_0n$，便有
$$
\begin{aligned}
\lambda_k(s,h)
=V_ks+W_k
-4\sum_{N\ge1}\frac{e^{-Ns/p}}N
\sum_{d_0\mid N}d_0
\sum_{y:(d_0\bmod p,y)\in R_k}
\cos\left(\frac{\pi hN}{p}+\frac{2\pi yN}{d_0p}\right).
\end{aligned}
$$
由 (1.3) 的 $y\mapsto-y$ 对称性，所有正弦项成对抵消。定义
$$
\boxed{
S_{k,N}=\sum_{d_0\mid N}d_0
\sum_{y:(d_0\bmod p,y)\in R_k}
\cos\left(\frac{2\pi yN}{d_0p}\right).
}                                                        \tag{3.3}
$$
得到根会话实现的精确公式
$$
\boxed{
\lambda_k(s,h)=V_ks+W_k
-4\sum_{N\ge1}
\frac{\cos(\pi hN/p)}N\,S_{k,N}e^{-Ns/p}.
}                                                        \tag{3.4}
$$
指数 $N/d_0$ 是整数；程序可以先在模 $p$ 中计算它和 $y$ 的乘积。$d_0$ 被 $p$ 整除时也包括在内，此时使用 $x=0$ 的目标行，且已排除的常数项不会重新出现，因为 $d_0>0$。

## 4. 相位折半是恒等式，不是假设曲线有额外单调性

对任意整数 $N$，
$$
\cos\left(\frac{\pi(2p-h)N}{p}\right)
=\cos\left(2\pi N-\frac{\pi hN}{p}\right)
=\cos(\pi hN/p).
$$
因此逐项有
$$\boxed{\lambda_k(s,2p-h)=\lambda_k(s,h).}               \tag{4.1}$$
作用正确的对数矩阵逆 $A$ 后，所有整数指数坐标
$$\gamma_j(s,h)=(A\lambda(s,h))_j$$
也相同。同时 $2p-h$ 与 $h$ 奇偶相同，故 $q$ 的正负号和相应 $j(q)$ 也相同。

所以
$$\boxed{h=0,1,\ldots,p}                                 \tag{4.2}$$
是全部 $2p$ 相位的完整代表集：$h=0,p$ 自己固定，其余两两配对。这正好是 $p+1$ 个相位；不能误减成只取偶数或只取奇数，也不需要声称原曲线的点在这些分支上实际一一相同。对必要整数格条件与整数 $j$ 来说，(4.1) 已足够。

## 5. 系数、函数尾项及导数尾项的严格界

每个固定第一坐标至多四个 $y$，故
$$
|S_{k,N}|\le4\sum_{d_0\mid N}d_0
\le4\sum_{d_0=1}^N d_0=2N(N+1).
$$
记 R101 已认证的
$$\kappa\ge\max_j\sum_k|A_{jk}|.$$
因此 $\gamma_j$ 中第 $N$ 个指数项的系数（含 $-4/N$、不含相位余弦）满足
$$\boxed{|C_{j,N}|\le8\kappa(N+1).}                      \tag{5.1}$$

置 $t=e^{-s/p}$，截断到 $N=J$，令 $u=J+1$。函数尾项的统一界是
$$
\boxed{
R_0(s)=8\kappa\,t^u
\frac{(u+1)-ut}{(1-t)^2}.
}                                                        \tag{5.2}
$$
这是 $\sum_{N\ge u}8\kappa(N+1)t^N$ 的精确几何级数和。它在 $s>0$ 严格递减，所以对 $s\in[a,b]$ 使用 $R_0(a)$ 安全。

对 $s$ 求一次导数，每项另乘 $-N/p$。可用没有负系数的表达式
$$
\boxed{
R_1(s)=\frac{8\kappa}{p}t^u
\left[
\frac{u(u+1)}{1-t}
+\frac{(2u+1)t}{(1-t)^2}
+\frac{t(1+t)}{(1-t)^3}
\right].
}                                                        \tag{5.3}
$$
对二次导数，可用
$$
\boxed{
\begin{aligned}
R_2(s)=\frac{8\kappa}{p^2}t^u\bigg[
&\frac{u^2(u+1)}{1-t}
+\frac{(3u^2+2u)t}{(1-t)^2}\\
&+\frac{(3u+1)t(1+t)}{(1-t)^3}
+\frac{t(1+4t+t^2)}{(1-t)^4}
\bigg].
\end{aligned}}                                           \tag{5.4}
$$
一般 $r$ 次导数尾界为
$$
R_r(s)\le8\kappa p^{-r}
\sum_{N\ge u}(N+1)N^rt^N.
$$
任何固定阶数的导数都在 $s\ge s_0>0$ 上一致绝对收敛，因此逐项求导有充分理由。

当前覆盖器的浮点导数只用于选择先检查哪个坐标，未用于排除叶子；在这种实现下，不需要把这个浮点导数包装成证明。若后续用导数做收缩或单调性判定，必须同时加入 (5.3) 或相应严格导数尾界。

## 6. 自然区间叶判据为什么覆盖全部潜在整数点

设节点是有理闭区间 $I=[a,b]$，已有完整层上界。严格区间运算给
$$
t(I)=\exp(-I/p).
$$
对每个坐标，用
$$
\delta_jI+\theta_j+
\sum_{N=1}^J C_{j,N}\cos(\pi hN/p)t(I)^N
+[-R_0(a),R_0(a)]                                       \tag{6.1}
$$
包住整条曲线的该坐标。这里的自然区间可能宽，但只会降低效率，不会漏掉真实值。

若 (6.1) 的整数下界大于整数上界，即
$$\lceil\inf(6.1)\rceil>\lfloor\sup(6.1)\rfloor,$$
则这整个节点中不存在整数指数向量，故没有所求整点。无需假设任何坐标单调、导数不变号或局部解唯一。

另一个合法叶条件是先严格包围 $j((-1)^he^{-s})$：

- 若包围没有整数，整节点没有整数 $j$；
- 若包围只含一个整数 $J_0$，则该节点内全部潜在整点的 $j$ 都只能是 $J_0$，把 $J_0$ 纳入后续准确判定即可。

第二种情况不宣称存在一个点，也不需要证明所有指数坐标均为整数。它只是一个完备候选收集步骤。

浮点值、浮点导数、与最近整数的浮点距离，可以用于坐标排序或分裂策略；任何真正排除都必须由 (6.1) 或严格 $j$ 包围决定。当前审读脚本符合这个分工。

最终证书还必须核对完整树覆盖。以根区间 $[L,S]$ 的 dyadic 节点 $(n,k)$ 表示
$$
[L+(S-L)k/2^n,\ L+(S-L)(k+1)/2^n].
$$
全部叶应构成前缀完备的二叉划分，或等价地在一个共同 dyadic 深度上精确覆盖根区间，不能有空隙。每个叶都须属于上述已证明的排除或单整数候选类型；`unresolved` 叶即为尚未完成，不能计入成功。每个尖点和 (4.2) 的每个相位都要有这样的完整证书。

## 7. 当前 $j$ 包围所用的两个尾界也成立

对实 $q=\pm e^{-s}$，记 $r=|q|<1$。使用
$$
j(q)=\frac{E_4(q)^3}{q}\prod_{n\ge1}(1-q^n)^{-24},
\qquad
E_4(q)=1+240\sum_{n\ge1}\sigma_3(n)q^n.
$$
因为 $\sigma_3(n)\le\zeta(3)n^3<2n^3$，截断到 $N$ 后有
$$
\left|E_4(q)-1-240\sum_{n=1}^N\sigma_3(n)q^n\right|
\le480\sum_{n>N}n^3r^n.
$$
写 $n=N+m$，$m\ge1$，则
$$n^3\le(N+1)^3m^3.$$
所以可用实现中的安全界
$$
\boxed{
E_{\rm tail}\le
480(N+1)^3r^{N+1}
\frac{1+4r+r^2}{(1-r)^4}.
}                                                        \tag{7.1}
$$

Euler 积的剩余部分为正实数，因为所有 $1-q^n>0$。其对数满足
$$
\begin{aligned}
\left|\log\prod_{n>N}(1-q^n)^{-24}\right|
&\le24\sum_{n>N}\frac{r^n}{1-r^n}\\
&\le\frac{24r^{N+1}}{(1-r)^2}.
\end{aligned}
$$
故
$$
\boxed{
\prod_{n>N}(1-q^n)^{-24}
\in
\exp\left[
-\frac{24r^{N+1}}{(1-r)^2},
\frac{24r^{N+1}}{(1-r)^2}
\right].
}                                                        \tag{7.2}
$$
用 $r$ 的严格上端代入两式即可覆盖整个节点。有限区间 $s\le S$ 使 $q$ 不为零，故最后除以 $q$ 合法。$E_4$ 在 CM 端点可能为零不影响普通多项式立方的区间包围，不能据此删掉端点。

## 8. 来源、已核与未核

- R101：单位指数的真正整数性、正确的对数矩阵方向、全部尖点及最新全局上界；中间 $1727$ 个整数 $j$ 的点数证书需一起接入。
- A. Bajolet、Y. Bilu、B. Matschke，*Computing integral points on $X_{\rm ns}^+(p)$*，[作者 v4](https://arxiv.org/html/1212.0665v4)，§2.1 的全部 $\sigma_cT^r$ 代表、Proposition 2.3 的实 $j$ 三段，以及 §4.1 的 Siegel 乘积。这些基本恒等式已独立逐项用于上面的推导；没有援引该文 Theorem 1.1 的整点分类。
- 本笔记已核公式与当前搜索器的每类判断逻辑；尚未在此声称所有尖点的覆盖文件都已生成或独立复算通过。最终小层分类必须由完成后的每尖点/每相位证书和全部候选的准确算术判定共同给出。

