# R98：三个小层必须出现新的四阶惯性素数

日期：2026-11-12；会话：serre-uniformity-resume2。

**状态：已证明，附全部 396 个 Thue 方程的无 GRH 认证解集。** 本文处理 $p=47,59,83$、商域 $\mathbb Q(\sqrt{-3})$、实际三次商准确导子 $6$ 或 $9$ 的一个完整子分支：如果 $2,3,p$ 以外没有四阶有限惯性，则只能有 $j=0$。因此剩余无 CM 曲线必须有一个新的四阶惯性素数。本文不排除含这种素数的曲线，不把三个固定层的子分支排除写成 Serre 一致性。

## 1. 准确结论

设 $E/\mathbb Q$，$p\in\{47,59,83\}$，实际模 $p$ 像为完整非分裂 Cartan 正规化子 $N$，其中 $C\simeq\mathbb F_{p^2}^{\times}$，且
$$
K=\mathbb Q(\sqrt{-3}),\qquad
\rho_{E,p}(I_p)=C^3,\qquad
c(\eta)\in\{6,9\},\qquad j(E)\in\mathbb Z.                 \tag{98.1}
$$
这里 $\eta=\lambda^{(p^2-1)/3}$ 是 R66 的实际三次角色，$c(\eta)$ 是其准确环类导子。设 $q\ne p$ 时的实际有限惯性商为 $\Gamma_q$。

**定理 98.1。** 若还满足
$$
|\Gamma_q|\ne4\quad\text{对每个 }q\ge5,\ q\ne p,           \tag{98.2}
$$
则
$$
\boxed{j(E)=0.}                                           \tag{98.3}
$$

**推论 98.2。** 对上述三个层数，任意无 CM 的实际曲线若满足完整正规化子像、$K=\mathbb Q(\sqrt{-3})$、小惯性及 $c(\eta)=6$ 或 $9$，就存在素数 $q\ge5$、$q\ne p$，使
$$
\boxed{
|\Gamma_q|=4,\qquad
v_q(j-1728)\text{ 为奇数},\qquad
q\equiv1\text{ 或 }11\pmod{12}.
}                                                        \tag{98.4}
$$
这里不必额外假设整 $j$：两个序的环类数均为三，R90 的非消失与 R92 的 Fourier 单位理想经 R69/R72 给出整性。

证明中保留 $j=0$ 这一 CM 值。$j=1728$ 在下面的 $p$ 次赋值条件处即被排除；对其他候选值不预先作 CM 分类，而逐一使用实际 Frobenius 矛盾。

## 2. 无四阶惯性把平方类固定为两种

整 $j$ 保证每个有限处潜在好约化。对 $q\ge5$、$q\ne p$，有限惯性阶属于
$$1,2,3,4,6,$$
且温和公式为
$$
|\Gamma_q|=\frac{12}{\gcd(12,v_q(\Delta))}.                \tag{98.5}
$$
这里 $\Delta$ 是全局最小判别式；其平方类、三次类均与所选有理模型无关。有限惯性在模 $p$ 上忠实，故 (98.2) 正是排除式 (98.5) 中的阶四情形。其他四个阶都迫使 $v_q(\Delta)$ 为偶数。

R66 已从小惯性证明 $p$ 处的最小好约化分歧指数为三或六。由于 $p>3$，同一温和公式给
$$v_p(\Delta)\equiv2,4,8,10\pmod{12},$$
也为偶数。因此全局平方类只能是
$$
[\Delta]\in\{\pm1,\pm2,\pm3,\pm6\}
\subset\mathbb Q^\times/\mathbb Q^{\times2}.              \tag{98.6}
$$

R96 的实际局部同域论证在 $c=6,9$ 两种情形均给
$$\Delta\in-3\mathbb Q_3^{\times2}.$$
三进赋值必须为奇数，且去掉全部三幂后的单位模三为负一。在 (98.6) 中只有
$$\boxed{[\Delta]=-3\quad\text{或}\quad[\Delta]=6}          \tag{98.7}$$
满足这两个条件。

由 $j-1728=c_6^2/\Delta$，有
$$
j-1728=-3Y^2\quad\text{或}\quad j-1728=6Y^2,\qquad Y\in\mathbb Z.
                                                               \tag{98.8}
$$
这里确实得到整数 $Y$：若整数等于一个平方自由整数乘有理数的平方，任何分母素数都使右边赋值为负，矛盾。

统一写成
$$
j-1728=-3mY^2,\qquad m\in\{1,-2\}.                       \tag{98.9}
$$

## 3. 三次类及固定实部

先假设 $j\ne0$。R96 的三次支撑和 $j=c_4^3/\Delta$ 给
$$
j=dX^3,\qquad X\in\mathbb Z,                             \tag{98.10}
$$
其中参数恰在以下必要集合中：

| 准确导子 $c$ | $d$ | 指数范围 | 参数数 |
|---:|---|---|---:|
| $6$ | $2^a3^bp^r$ | $a,r\in\{1,2\},\ b\in\{0,1\}$ | $8$ |
| $9$ | $3^bp^r$ | $a=0,\ b,r\in\{1,2\}$ | $4$ |

$d$ 是正的无三次因子整数；负号可吸收入 $X^3$。由 $j$ 整性，$X$ 必为整数：$v_\ell(d)\in\{0,1,2\}$，故 $v_\ell(X)<0$ 将使 $v_\ell(j)<0$。尤其
$$p\mid j,$$
所以 $j=1728$ 不在此分支。

将 (98.9) 与 (98.10) 合并：
$$dX^3=3(576-mY^2).$$
令
$$
b'=(b-1)\bmod3\in\{0,1,2\},\qquad
D_0=2^a3^{b'}p^r.
$$
若 $b=0$，模三先给 $3\mid X$，令 $X=3Z$；若 $b=1,2$，令 $X=Z$。两种情况下都得到
$$
\boxed{576-mY^2=D_0Z^3,\qquad Y,Z\in\mathbb Z.}           \tag{98.11}
$$
反向恢复 $X$ 的规则同上。由于已把 $j=0$ 单独保留，进行以下素因子分解时可以假设 $Z\ne0$。

R96 对 $v_3(j)$ 还有更强限制；本证明不需用它们删掉方程。保留整个必要集合使覆盖更直接。

## 4. $m=-2$：虚二次 PID 中的完整归约

写 $s=\sqrt{-2}$。整环 $\mathbb Z[s]$ 的范数为 $u^2+2v^2$。它是范数欧几里得环：商的两个坐标各取最近整数，误差范数至多 $3/4<1$。故它是 PID，单位只有 $\pm1$，而这两个单位都是三次幂。

令
$$\gamma=24+Ys,\qquad N\gamma=576+2Y^2=D_0Z^3.$$
任何同时整除 $\gamma$、$\bar\gamma$ 的素理想都整除
$$\gamma+\bar\gamma=48.$$
因此 $p>3$ 上方的素理想不能同时出现。

### 4.1 层 $47$ 的十二个参数分支直接不可能

$(-2/47)=-1$，故 $(47)$ 在 $\mathbb Z[s]$ 中为素理想。若 $47\mid N\gamma$，在剩余域 $\mathbb F_{47^2}$ 中的范数为零，必有 $\gamma=0$，于是 $47\mid24$，矛盾。

因此 $p=47,m=-2$ 时，全部十二个 $(c,a,b,r)$ 参数分支都不可能。这里没有留下一组尚未求解的 Thue 方程。

### 4.2 层 $59,83$ 的素因子取向和全部方程

其余两个层在 $\mathbb Q(s)$ 分裂，可选
$$
\pi_{59}=3+5s,\quad N\pi_{59}=59,\qquad
\pi_{83}=9+s,\quad N\pi_{83}=83.
$$
又取
$$
\pi_2=s,\quad N\pi_2=2,\qquad
\pi_{3,+}=1+s,\quad\pi_{3,-}=1-s,\quad N\pi_{3,\pm}=3.
$$

在 $p$ 上方只有一个素理想整除 $\gamma$；用 $Y\mapsto-Y$ 可使它对应 $\pi_p$，不损失所恢复的 $j$。其他不在 $2,3,p$ 上方的素理想，其在 $\gamma$ 中的指数都是三的倍数：分裂素数利用共轭不同时整除；惰性素数的范数指数为二倍，二与三互素。因而去掉三次幂后，必可写成
$$
\gamma=\delta(U+Vs)^3,\qquad U,V\in\mathbb Z,              \tag{98.12}
$$
其中
$$
\delta=\pi_2^a\pi_p^r\pi_{3,+}^{k_1}\pi_{3,-}^{k_2},
\quad 0\le k_1,k_2\le2,\quad k_1+k_2\equiv b'\pmod3.      \tag{98.13}
$$
每个参数恰有三组 $(k_1,k_2)$。$\pi_2$ 处的指数模三为 $a$，因为它的范数为二；三处只要求两取向的指数和模三为 $b'$。所有单位已吸收入三次幂。

写 $\delta=S+Ts$。取 (98.12) 实部，得到
$$
\boxed{SU^3-6TU^2V-6SUV^2+4TV^3=24.}                    \tag{98.14}
$$
因此每个层有 $12\cdot3=36$ 个方程。

这些二元三次型都不可约。若有有理零点 $[U:V]$，则在 $\mathbb Q(s)$ 中
$$
\frac{\delta}{\bar\delta}
=-\left(\frac{U-Vs}{U+Vs}\right)^3.
$$
左边在选定 $p$ 素理想的赋值为 $r=1$ 或 $2$，不可能为三的倍数。相同理由也说明 $S\ne0$，所以不存在因首项消失而遗漏的无穷远零点。

恢复也完全显式。$N\delta/D_0$ 是正整数的立方，写成 $w^3$，则
$$
\begin{aligned}
A&=U^3-6UV^2,& B&=3U^2V-2V^3,\\
Y&=SB+TA,& Z&=w(U^2+2V^2).
\end{aligned}                                           \tag{98.15}
$$
式 (98.14) 给 $SA-2TB=24$。这些恢复恒等式由整数算术逐解复核。

## 5. $m=1$：分裂二次代数中的完整归约

此时
$$
(24+Y)(24-Y)=D_0Z^3,\qquad
\gcd(24+Y,24-Y)\mid48.                                  \tag{98.16}
$$
因为 $p>3$，恰有一个因子被 $p$ 整除；交换 $Y$ 的符号可令它为第一个。对 $2,3,p$ 以外的素数，出现在非零两因子中的指数均为三的倍数。负号吸收入整数立方，所以存在整数 $U,V$ 使
$$
24+Y=d_1U^3,\qquad24-Y=d_2V^3,                           \tag{98.17}
$$
其中
$$
\begin{aligned}
d_1&=2^{i_1}3^{k_1}p^r,&d_2&=2^{i_2}3^{k_2},\\
0\le i_1,i_2,k_1,k_2&\le2,&
i_1+i_2&\equiv a\pmod3,\quad
k_1+k_2\equiv b'\pmod3.
\end{aligned}                                           \tag{98.18}
$$
每条同余分别有三组解，故每个参数给九个方程
$$
\boxed{d_1U^3+d_2V^3=48.}                               \tag{98.19}
$$
每层共 $12\cdot9=108$ 个。

这些型也不可约：$-d_2/d_1$ 在 $p$ 的赋值为 $-r$，不是有理数的立方。若 $d_1d_2/D_0=w^3$，恢复公式为
$$
Y=\frac{d_1U^3-d_2V^3}{2},\qquad Z=wUV.                 \tag{98.20}
$$
式 (98.19) 保证分子为偶数。即便计算返回 $U=0$ 或 $V=0$，恢复的也是预先保留的 $j=0$，不会因此丢失非零解。

至此完整的计算规模为：

| $p$ | $m=1$ | $m=-2$ | 实际 Thue 方程总数 | 由惰性直接排除的参数分支 |
|---:|---:|---:|---:|---:|
| $47$ | $108$ | $0$ | $108$ | $12$ |
| $59$ | $108$ | $36$ | $144$ | $0$ |
| $83$ | $108$ | $36$ | $144$ | $0$ |
| 合计 | $324$ | $72$ | $396$ | $12$ |

没有把 $p=47$ 的惰性分支计作已运行的方程，也没有把最初的形式参数数误写成实际求解次数。

## 6. 全部认证解和每个非零候选的反证

每个不可约三次多项式都通过
$$\texttt{T=thueinit(P,1); S=thue(T,rhs)}$$
求全部整数解。PARI 的标志 $1$ 明确要求无 GRH 认证；未使用默认的条件性初始化，也未用有限高度搜索判断无解。

完整结果为：层 $47$ 有十七组整数解，层 $59$ 有十五组，层 $83$ 有十七组，总计四十九组。逐解代回 (98.14)/(98.19)，再通过 (98.15)/(98.20) 以及第 3 节的 $X$ 恢复规则，得到下表列出的全部非零 $j$。另在每层保留 $j=0$。

| $p$ | 非零 $j$ | 反证素数 $q$ | $j\bmod q$ | 实际模型的 $a_q$ |
|---:|---:|---:|---:|---:|
| $47$ | $-974592000$ | $11$ | $3$ | $-6$ |
| $47$ | $-232952304$ | $5$ | $1$ | $2$ |
| $47$ | $-15593472$ | $11$ | $7$ | $-2$ |
| $47$ | $-475875$ | $11$ | $7$ | $-2$ |
| $47$ | $141$ | $5$ | $1$ | $2$ |
| $59$ | $11328$ | $11$ | $9$ | $-2$ |
| $59$ | $38232$ | $5$ | $2$ | $3$ |
| $59$ | $222969024$ | $5$ | $4$ | $-1$ |
| $83$ | $-1357492224$ | $5$ | $1$ | $2$ |
| $83$ | $-430272000$ | $11$ | $7$ | $-2$ |
| $83$ | $-11617344$ | $5$ | $1$ | $2$ |
| $83$ | $71712$ | $5$ | $2$ | $3$ |
| $83$ | $121014$ | $5$ | $4$ | $-1$ |

### 6.1 为什么这些是实际曲线的矛盾

对任一候选 $j\ne0,1728$，取有理模型
$$
F_j:\quad y^2+xy=x^3-\frac{36}{j-1728}x-\frac1{j-1728}.
                                                               \tag{98.21}
$$
直接计算给
$$c_4=\frac{j}{j-1728},\qquad
\Delta=\frac{j^2}{(j-1728)^3},$$
故它的 $j$ 不变量正是 $j$。所有同 $j$ 的有理椭圆曲线都是它的二次扭曲。

表中每个 $q$ 都满足
$$q\ne p,\qquad q\equiv2\pmod3,\qquad q\nmid j(j-1728).$$
因此 $F_j$ 在 $q$ 有好约化，且 $q$ 惰性于商域 $K$。二次扭曲只把模 $p$ 矩阵乘以中心标量 $\pm1$，不会改变 $N/C$ 商域。所以 $F_j$ 的 Frobenius 仍落在 $N\setminus C$，矩阵迹必须为零：
$$a_q(F_j)\equiv0\pmod p.                                \tag{98.22}$$
但表中每个迹均非零，且绝对值小于对应的 $p$，矛盾。这里不需要假设原曲线在 $q$ 本来有好约化；可以对同 $j$ 的好约化扭曲使用 (98.22)。

### 6.2 点数为完全整数计算

在 $\mathbb F_q$ 中令 $a_4=-36/(j-1728)$、$a_6=-1/(j-1728)$。固定 $x$ 后，关于 $y$ 的二次方程的判别式为
$$D_x=x^2+4(x^3+a_4x+a_6).$$
于是
$$
a_q(F_j)=-\sum_{x\in\mathbb F_q}\left(\frac{D_x}{q}\right).       \tag{98.23}
$$
证书存每个 $D_x$ 的 Legendre 符号、$a_4,a_6$ 和最终迹；所有值用标准库模幂、整数加法重算。所需素数只有五和十一，故点数反证也能逐项手算复核。

因此全部非零 $j$ 被排除，定理 98.1 得证。

## 7. 新四阶素数的算术范围

现设 $E$ 无 CM，且满足推论 98.2 的其他前提。由 R90/R92 得 $j$ 整；若没有 (98.4) 的四阶素数，定理 98.1 给 $j=0$，与无 CM 矛盾。故存在 $q\ge5,q\ne p$ 使 $|\Gamma_q|=4$。

由 (98.5)，$v_q(\Delta)$ 为奇数；恒等式
$$j-1728=c_6^2/\Delta$$
使 $v_q(j-1728)$ 也为奇数。$j$ 整保证该赋值非负，故它实际为正。

$q$ 不分歧于 $K$，所以有限惯性在 $C$ 内。取其阶四生成元 $s$ 及 Frobenius 提升 $g$，温和关系为
$$gsg^{-1}=s^q.$$
若 $q$ 在 $K$ 分裂，$g\in C$ 与 $s$ 交换，故 $q\equiv1\pmod4$；同时 $q\equiv1\pmod3$，所以 $q\equiv1\pmod{12}$。
若 $q$ 在 $K$ 惰性，$g\in N\setminus C$ 的共轭作用是 $s\mapsto s^p$。三个层数均满足 $p\equiv-1\pmod4$，故 $q\equiv-1\pmod4$；结合 $q\equiv-1\pmod3$ 得 $q\equiv11\pmod{12}$。这证明 (98.4)。

还可准确接到 R21 的类数一比较：取 CM 参考曲线 $A:y^2=x^3+1$，在 $K$ 上选择相容的 $p$ 处取向，差字符 $\beta=\lambda_E/\lambda_A$ 满足 $\beta^{12}=1$。$A$ 在这些 $q$ 有好约化，故 $\beta(I_q)$ 恰有阶四，$\beta^3$ 的四次部分在该处真正分歧。它不能由二次扭曲消去；乘以 $\pm1$ 仍保持阶四。因而本结果逼出的是实际变化的四次分歧，不只是一个无关辅助域的素因子。

本文没有证明这种四次角色不存在，也没有给它的导子上界。一般整数范数
$$j-1728=U^2-3V^2$$
仍允许两坐标都变化；相应无界必要族已在[范数笔记](../notes/2026-11-12-remaining-levels-real-quadratic-norm-resume2.md)明确记录，不能当成实际曲线族或排除定理。

## 8. 可复算文件与数据范围

- [Python 验证器](../scripts/verify_small_levels_quartic_ramification.py)：生成全部参数和不可约三次型，调用认证求解，逐解恢复 $j$，重算每个 Frobenius 反证。
- [PARI/GP 核心](../scripts/small_levels_quartic_ramification_thue.gp)：每一式检查不可约性，再运行 $\texttt{thueinit(P,1)}$。
- [完整 JSON](../scripts/data/small_levels_quartic_ramification.json)：全部 396 个方程、包括空集在内的全部解集、49 组恢复数据、12 个惰性排除分支以及十三条反证。

运行：
~~~sh
python -B topics/serre-uniformity/scripts/verify_small_levels_quartic_ramification.py --gp /tmp/pari-2.19.0/gp
~~~
默认重新求解全部方程，并逐字节比较 JSON；$\texttt{--write}$ 重新生成证书。参考执行版本为 PARI/GP 2.19.0。证书大小 196912 字节，SHA256：
~~~text
03b7f13031b2472e354b60f8cf67d1a896dc01e000c690066fc46aca1fb08e78
~~~
源码和数据均在环境恢复后重新计算；没有把重置前未完成的运行当作计算结果。

## 9. 输入来源与边界

- [R66](R66-cubic-conductor-nonvanishing-and-tate-primes.md) §2：实际小惯性 $C^3$ 及 $p$ 处三/六阶好约化分歧。
- [R96](R96-actual-cubic-discriminant-support-and-local-three-branches.md)：准确三次支撑和 $\Delta\in-3\mathbb Q_3^{\times2}$；不省略整 $j$ 前提。
- [R90](R90-class-number-three-periods-and-actual-frobenius-exclusions.md)、[R92](R92-small-level-fourier-units-and-actual-integrality.md)、[R72](R72-optimal-quotient-cusp-immersion-and-exceptional-denominators.md)：此实际环类数三分支在三个层数的整性。
- [R21](R21-twelfth-power-signature-and-cm-twists.md)：类数一 CM 比较及差字符的十二次幂。
- J.-P. Serre，*Propriétés galoisiennes des points d'ordre fini des courbes elliptiques*，Invent. Math. **15** (1972)，§5.6，pp. 311–312：[作者原文](https://www.college-de-france.fr/media/jean-pierre-serre/UPL5874918517843398173_Serre_proprie_te_s_galoisiennes_des_courbes_elliptiques.pdf)。有限惯性及温和阶公式也已在 R21/R66/R96 的实际模型接口中核准。
- PARI/GP 官方文档，[*Polynomials and power series*](https://pari.math.u-bordeaux.fr/dochtml/html-stable/Polynomials_and_power_series.html)，$\texttt{thue}$、$\texttt{thueinit}$ 条目：$\texttt{thue}$ 给全部整数解，初始化标志一给无 GRH 认证。不可约覆盖、恢复及模素数反证在本文独立展开。

本结果不用 BBM 的整点算法结论，不使用未发表的整性定理；它完成的是 (98.2) 子分支。仍有新四阶素数的实际曲线以及一般层数、一般环类数均未在这里排除。
