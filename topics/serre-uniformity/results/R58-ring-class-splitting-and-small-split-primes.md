# R58：一模十二指数的二次惯性型、环类分裂与小素数理想阶界

日期：2026-11-12；会话：serre-uniformity-resume2。

**状态：已证明的全局必要条件。** 本文对 $p\equiv1\pmod{12}$ 将 R21 的十二次幂特征降为二次幂，证明一个环类群正合列必须分裂。实际椭圆曲线的整数 Frobenius 迹进一步给出：若分裂素数 $q$ 上方的理想类非主、阶为 $r$，则 $p<4q^{r/2}$。这同时适用于 $q=2,3$，并导出明确的变化商域判别式增长下界。所有结论均无条件；未假定类数一，也未把残余表示提升为有理系数的 CM 特征零表示。商域仍可增长，所以主要目标尚未解决。

## 1. 假设、记号与结论

设 $E/\mathbb Q$ 无 CM，
$$
p>37,\qquad p\equiv1\pmod{12},\qquad
\operatorname{Im}\bar\rho_{E,p}=N_{\rm ns}(p).
\tag{58.1}
$$
令 $C\simeq\mathbb F_{p^2}^{\times}$ 为完整非分裂 Cartan，$K$ 为商特征的二次域。R5 已证明：$K$ 虚二次，$p$ 在 $K$ 中不分歧且惰性。

固定识别 $C\simeq\mathbb F_{p^2}^{\times}$，得到
$$
\lambda:G_K\twoheadrightarrow\mathbb F_{p^2}^{\times},
\qquad
\lambda^{p+1}=\chi_p|_{G_K},
\qquad \lambda^c=\lambda^p.
$$
本文始终使用不同记号
$$
\boxed{\mu=\lambda^2,\qquad
\nu=\mu/\chi_p=\lambda^{1-p},\qquad
U=\ker(N:\mathbb F_{p^2}^{\times}\to\mathbb F_p^\times).}
\tag{58.2}
$$
所以 $\nu$ 取值于阶 $p+1$ 的循环群 $U$。

设 $D=|D_K|$、$h=h_K$，$\mathcal O_p=\mathbb Z+p\mathcal O_K$。记 $H$ 为 $K$ 的 Hilbert 类域，$H_p$ 为序 $\mathcal O_p$ 的环类域，$M$ 为模 $p$ 表示的项目除法域。

**定理 R58。**

1. $\mu$ 在全部 $w\nmid p$ 处不分歧，包括 $2,3$ 上方；选取两个剩余域嵌入中的一个后，
   $$
   \mu|_{I_p}=\omega_2^2.
   \tag{58.3}
   $$
   $\nu$ 的导子恰为 $p\mathcal O_K$，在该素数处的惯性像为整个 $U$。

2. 环类群的标准正合列
   $$
   1\longrightarrow
   \mathbb F_{p^2}^{\times}/\mathbb F_p^\times
   \longrightarrow\operatorname{Pic}(\mathcal O_p)
   \longrightarrow\operatorname{Cl}(K)\longrightarrow1
   $$
   必须分裂。因此
   $$
   \boxed{\operatorname{Pic}(\mathcal O_p)
   \simeq C_{p+1}\times\operatorname{Cl}(K),\qquad
   H_p=HM,\qquad H\cap M=K.}
   \tag{58.4}
   $$
   这里的直积分解不声称规范。

3. 若 $q$ 为在 $K$ 中分裂的任意有理素数，
   $$
   q\mathcal O_K=\mathfrak q\bar{\mathfrak q},\qquad
   r=\operatorname{ord}[\mathfrak q],\qquad
   \mathfrak q^r=(\alpha),
   $$
   则有必要条件
   $$
   \boxed{
   (\alpha/\bar\alpha)^{(p+1)/\gcd(r,p+1)}
   \equiv1\pmod{p\mathcal O_K}.}
   \tag{58.5}
   $$
   若 $[\mathfrak q]\ne1$，则更强地
   $$
   \boxed{p<4q^{r/2},\qquad
   r>\frac{2\log(p/4)}{\log q}.}
   \tag{58.6}
   $$
   这里没有 $q\ge5$ 或预先好约化的附加条件。

4. 若 $h>1$，则
   $$
   \boxed{
   p<4(2D^{5/2})^{h/2},}
   \tag{58.7}
   $$
   并有完全显式的后果
   $$
   \boxed{
   \log(p/4)
   <
   \frac{\sqrt D}{\pi}
   \left(1+\log\left(\frac{2\sqrt D}{\pi}\right)\right)
   \left(\log2+\frac52\log D\right).}
   \tag{58.8}
   $$
   这约束的是实际变化的商域；它是增长下界，并没有给出 $D$ 的绝对上界。

## 2. 全部 p 外惯性为什么只需平方

取 $K$ 的有限位 $w\nmid p$。

若 $E$ 潜在乘法约化，Tate 描述和像的阶与 $p$ 互素说明模 $p$ 惯性只剩标量 $\pm I$，故 $\lambda^2$ 在该处平凡。

若 $E$ 潜在好约化，$T_p(E)$ 的惯性像有限；其作用忠实嵌入取得好约化后的保原点自同构群。有限惯性像模 $p$ 的约化忠实：核在 $1+pM_2(\mathbb Z_p)$ 内，而后者在奇素数 $p$ 时无非平凡有限阶元素。模 $p$ 惯性已经落在循环群 $C$，所以特征零惯性也为循环群。

R21 §5 的自同构次数论证说明，一个这样的循环惯性群中所有元素的阶都整除 $12$。这一论证包含剩余特征 $2,3$，没有把整个可能非交换的自同构群的阶误当作整除 $12$。

又因 $w\nmid p$，行列式在惯性上平凡，所以
$$
\lambda(I_w)\subset U,\qquad
|\lambda(I_w)|\mid\gcd(12,p+1)=2.
$$
于是 $\mu=\lambda^2$ 在 $w$ 不分歧。这一推导适用于 $K/\mathbb Q$ 在该处有分歧的情况，也包括全部野惯性。

在后面 $q$ 分裂的局部应用中，$K_{\mathfrak q}=\mathbb Q_q$。上述忠实性还说明：若 $E/\mathbb Q_q$ 潜在好约化，则整个 $T_p(E)$ 惯性像为 $\{I\}$ 或 $\{\pm I\}$。阶二元素必为 $-I$，因为其行列式为一，且特征零中阶二矩阵半单。这将用于第 5 节，不能仅从“潜在好约化”直接跳到“二次好约化”。

## 3. p 处的准确平方惯性型与主理想公式

R15/R21 已给 $E$ 在 $p$ 潜在超奇异。R27 §4 的论证在当前同余类中适用：特征 $p$ 的 $j=0$ 和 $1728$ 都是普通的，所以取得好约化后的超奇异特殊纤维的自同构群只有 $\{\pm1\}$。最小好约化惯性次数因而为 $1$ 或 $2$；一个局部二次扭曲使 $E$ 在 $\mathbb Q_p$ 上好超奇异。

好超奇异、绝对分歧指数一的二级基本特征为 $\omega_2,\omega_2^p$。原来的至多二次扭曲在平方后消失，故
$$
\mu|_{I_p}\in\{\omega_2^2,\omega_2^{2p}\}.
$$
交换 $\lambda,\lambda^p$ 或等价地交换 $\mathcal O_K/p\simeq\mathbb F_{p^2}$ 的两个嵌入，便得到 (58.3)。

固定这个嵌入，并使用算术 Frobenius 的 Artin 约定。因为 $\mu$ 在 $p$ 外不分歧，在 $p$ 的单位上由 (58.3) 给出剩余元的逆平方，主 idèle 的全局互反关系给
$$
\boxed{\mu((\alpha))\equiv\alpha^2\pmod p}
\quad
\text{对所有在 }p\text{ 为单位的 }\alpha\in K^\times.
\tag{58.9}
$$
具体地，$p$ 外的均匀化参数贡献组成理想 $(\alpha)$ 的 Artin 符号，而 $p$ 单位处贡献为 $\widetilde\alpha^{-2}$，二者相乘为一。这里 $\widetilde\alpha$ 表示剩余元，$\bar\alpha$ 始终专指二次共轭。采用相反 Artin 约定会同时把全部特征取逆，不改变任何后续结论。

圆分特征在理想上为范数模 $p$，所以 (58.9) 给
$$
\boxed{\nu((\alpha))\equiv
\frac{\alpha^2}{N_{K/\mathbb Q}(\alpha)}
=\frac{\alpha}{\bar\alpha}\pmod p.}
\tag{58.10}
$$
由于 $p$ 惰性，剩余域中二次共轭恰为 $x\mapsto x^p$。

在 $p$ 惯性上，
$$
\nu|_{I_p}=\omega_2^{\,1-p}
$$
或其逆。此特征的阶恰为 $p+1$，与 $p$ 互素，故 $\nu$ 的导子恰为 $p\mathcal O_K$，并且全部 $U$ 都由惯性产生。

## 4. 环类群上为什么得到真正的直积分裂

$p\equiv1\pmod{12}$ 在 $\mathbb Q(i)$、$\mathbb Q(\sqrt{-3})$ 中都分裂，而在本题 $K$ 中惰性。因此
$$
K\ne\mathbb Q(i),\mathbb Q(\sqrt{-3}),\qquad
\mathcal O_K^\times=\{\pm1\}.
$$

序 $\mathcal O_p$ 的理想类群可用 $\mathcal O_K$ 的与 $p$ 互素理想描述：商去由那些模 $p$ 等于某个有理非零剩余元的 $\alpha$ 生成的主理想。由 (58.10)，$\nu$ 在这些主理想上平凡，所以它经过
$$
\nu:\operatorname{Pic}(\mathcal O_p)\longrightarrow U.
$$

标准序类群正合列的核为
$$
I=\frac{(\mathcal O_K/p)^\times}
{(\mathbb Z/p)^\times\operatorname{im}(\mathcal O_K^\times)}
=\frac{\mathbb F_{p^2}^\times}{\mathbb F_p^\times}.
$$
这里单位 $\pm1$ 已在分母的 $\mathbb F_p^\times$ 内，不留下额外的指数二或指数三。对由 $x\in\mathbb F_{p^2}^\times$ 表示的核元素，(58.10) 给
$$
\nu|_I:x\bmod\mathbb F_p^\times\longmapsto x^{1-p}.
\tag{58.11}
$$
这个映射的核恰为 $\mathbb F_p^\times$，像恰为 $U$，因此是两个阶 $p+1$ 群之间的同构。

于是 $\nu$ 是正合列核上的一个回缩，直接给出
$$
\operatorname{Pic}(\mathcal O_p)=I\times\ker\nu,
\qquad \ker\nu\simeq\operatorname{Cl}(K).
$$
这证明 (58.4) 的群论部分。特别地，还得到
$$
\exp\operatorname{Pic}(\mathcal O_p)
=\operatorname{lcm}(p+1,\exp\operatorname{Cl}(K)).
$$

$\nu=\lambda^{1-p}$ 恰杀死 Cartan 的全部 $\mathbb F_p^\times$ 标量；所以它切出的扩张是项目除法域 $M/K$，次数 $p+1$。第 3 节说明它在 $p$ 全分歧，因此与处处不分歧的 $H/K$ 相交为 $K$。又 $M\subset H_p$，而
$$
[HM:K]=h(p+1)=[H_p:K],
$$
故 $H_p=HM$。

最后，对 $\mathfrak q^r=(\alpha)$，由 (58.10)，
$$
\nu(\mathfrak q)^r\equiv\alpha/\bar\alpha\pmod p.
$$
$U$ 是阶 $p+1$ 的循环群，其 $r$ 次幂子群恰为被 $(p+1)/\gcd(r,p+1)$ 次幂杀死的子群。这证明 (58.5)。条件与 $\alpha$ 乘单位或交换 $\mathfrak q,\bar{\mathfrak q}$ 无关。

当 $\gcd(h,p+1)=1$ 时，该抽象正合列本来就按群阶互素分裂；不能把 (58.4) 在这种情形夸大为新的排除。下一节的整数迹条件则不止是正合列分裂。

## 5. 任意分裂素数处的真实局部椭圆曲线

固定分裂的有理素数 $q$。自动有 $q\ne p$，且
$$
\bar\rho_{E,p}(G_{\mathbb Q_q})\subset C.
$$
分两种约化情形处理。

### 5.1 潜在乘法约化

存在 $\mathbb Q_q$ 上的二次扭曲 $F$，使 $F$ 为分裂 Tate 曲线。该扭曲只乘标量 $\pm I$，所以其残余像仍在 $C$。Tate Frobenius 的两个特征值为 $1,q$。

非分裂 Cartan 中若一个元素的特征值在 $\mathbb F_p$ 内，则它为标量。因此
$$
\boxed{q\equiv1\pmod p.}
\tag{58.12}
$$
若 $[\mathfrak q]\ne1$、$r\ge2$，这已经给
$$
p\le q-1<4q^{r/2}.
$$

### 5.2 潜在好约化，包括 q=2、3

第 2 节已证明 $T_p(E)$ 的整个惯性像为标量 $\{\pm I\}$ 的子群。由此定义惯性二次特征 $\tau_I$。因为标量与全部矩阵交换，$\tau_I$ 在 Frobenius 共轭下不变。

该惯性特征确实延拓为整个 $G_{\mathbb Q_q}$ 的二次特征：选取算术 Frobenius 的一个提升，其闭包给出到未分歧商 $\widehat{\mathbb Z}$ 的连续截面；在此截面上取值 $1$，在惯性上取 $\tau_I$。Frobenius 不变性保证所得乘法规则定义连续特征
$$
\tau:G_{\mathbb Q_q}\to\{\pm1\}.
$$
等价地，这是局部互反映射上将一个单位二次特征延拓到均匀化参数的选择。它在剩余特征 $2$ 时同样有效，没有使用“所有二次扩张都温和”之类错误断言。

局部二次扭曲 $F=E^\tau/\mathbb Q_q$ 的 $T_p$ 惯性平凡，由 Néron–Ogg–Shafarevich 判据，$F$ 在 $\mathbb Q_q$ 上好约化。于是有真正的整数
$$
a=a_q(F)\in\mathbb Z,\qquad |a|\le2\sqrt q,
$$
以及 Frobenius 多项式
$$
T^2-aT+q.
\tag{58.13}
$$
局部扭曲不改变平方特征 $\mu$。若 $\beta\in\mathbb F_{p^2}^\times$ 为 $F[p]$ 对应的一个 Frobenius 特征值，则
$$
\beta+\beta^p\equiv a,\qquad
\beta^{p+1}\equiv q,\qquad
\beta^2=\mu(\mathfrak q).
\tag{58.14}
$$
这里两支的共轭顺序由已固定的 $\lambda$ 决定；改变局部二次扭曲的不分歧部分至多把 $\beta,a$ 同时取负。

## 6. 从主理想同余取平方根，再利用整数迹

现假设 $[\mathfrak q]\ne1$，其阶为 $r\ge2$，并选
$$
\mathfrak q^r=(\alpha),\qquad
N_{K/\mathbb Q}(\alpha)=q^r.
$$
因为 $K$ 虚二次，
$$
|\alpha|=q^{r/2},\qquad
t=\operatorname{Tr}_{K/\mathbb Q}(\alpha)\in\mathbb Z.
$$
$\alpha$ 不可能为实数：若 $\alpha=\bar\alpha$，则主理想给
$\mathfrak q^r=\bar{\mathfrak q}^{\,r}$，违反不同素理想的唯一分解。同样，$\alpha$ 不能纯虚，因为 $\bar\alpha=-\alpha$ 也会使这两个主理想相同。因此
$$
0<|t|<2q^{r/2}.
\tag{58.15}
$$

在第 5.2 节的好约化分支，由 (58.9)、(58.14)，
$$
\beta^{2r}=\mu(\mathfrak q)^r
=\mu((\alpha))\equiv\alpha^2\pmod p.
$$
$p$ 奇，剩余域为真正的域，所以可以取平方根：
$$
\beta^r\equiv\epsilon\alpha\pmod p,\qquad
\epsilon\in\{1,-1\}.
\tag{58.16}
$$
施加剩余域的 $p$ 次幂给
$$
\beta^{pr}\equiv\epsilon\bar\alpha\pmod p.
$$
同一个 $\epsilon$ 被保留，因为 $\epsilon\in\mathbb F_p$。

令 $\pi,\bar\pi$ 为 (58.13) 在特征零中的两个根，取一支使约化为 $\beta$。定义整数递推
$$
T_0(a,q)=2,\quad T_1(a,q)=a,\quad
T_n(a,q)=aT_{n-1}(a,q)-qT_{n-2}(a,q).
$$
则 $T_r(a,q)=\pi^r+\bar\pi^r$，且 $|\pi|=|\bar\pi|=\sqrt q$。由 (58.16) 得
$$
\boxed{T_r(a,q)\equiv\epsilon t\pmod p.}
\tag{58.17}
$$

必须验证整数差不为零。假设 $T_r(a,q)=\epsilon t$。两组根的和与积相同：
$$
\{\pi^r,\bar\pi^r\}
=\{\epsilon\alpha,\epsilon\bar\alpha\},
$$
因为两边积均为 $q^r$。$\alpha$ 非实，故 $\pi^r$ 非实；于是
$$
\mathbb Q(\pi)=\mathbb Q(\pi^r)=K.
$$
这里 $\pi$ 为虚二次代数整数，因为 $a^2<4q$，而 $q$ 是素数，所以等号 $a^2=4q$ 不可能。比较理想，由 $\pi^r=\epsilon\alpha$ 或 $\epsilon\bar\alpha$ 得
$$
(\pi)^r=\mathfrak q^r
\quad\text{或}\quad
(\pi)^r=\bar{\mathfrak q}^{\,r}.
$$
理想群无挠，故 $\mathfrak q$ 或其共轭为主，矛盾。

因此 (58.17) 的差是非零整数，且
$$
p\le |T_r(a,q)-\epsilon t|
\le2q^{r/2}+|t|<4q^{r/2}.
\tag{58.18}
$$
结合潜在乘法分支即证明 (58.6)。只用 $\mu$ 得到的平方迹差会给较弱的 $4q^r$；(58.16) 保留的共同符号正是改进指数所需的信息。

还有一个完全整数的计算接口：
$$
\boxed{
p\mid(q-1)
\prod_{a=-\lfloor2\sqrt q\rfloor}^{\lfloor2\sqrt q\rfloor}
\bigl(T_r(a,q)^2-t^2\bigr).}
\tag{58.19}
$$
当 $\mathfrak q$ 非主时，每个乘积因子都非零，正是上面的理想论证。这个有限整数只依赖 $K,\mathfrak q,r,\alpha$；$\alpha$ 的符号不影响它。它没有把有限局部拟合当作实际曲线的构造。

## 7. 一个不使用 Chebotarev 或 GRH 的判别式增长界

假设 $h>1$。先证明存在一个非主分裂素理想 $\mathfrak q$，其下方有理素数满足
$$
q\le2D^{5/2}.
\tag{58.20}
$$

取一个非主理想类的正定原始约化二元二次型
$$
Q(x,y)=ax^2+bxy+cy^2,\qquad b^2-4ac=-D,
\qquad |b|\le a\le c.
$$
因此 $a\le\sqrt{D/3}<\sqrt D$，并有 $c=(D+b^2)/(4a)\le D$。

对每个素数 $\ell\mid D$，可以选择一个 $x\bmod\ell$ 使 $Q(x,1)\ne0\bmod\ell$。若 $\ell$ 奇且 $\ell\nmid a$，模 $\ell$ 判别式为零，所以至多一个坏根；若 $\ell\mid a$，则 $\ell\mid b$，由原始性得 $\ell\nmid c$。在 $\ell=2$ 且 $2\mid D$ 时，$b$ 偶；$a$ 奇时多项式模二为 $x+c$，$a$ 偶时 $c$ 奇，同样可选。

由中国剩余定理，取
$$
0\le x<\operatorname{rad}(D)\le D,\qquad
m=Q(x,1),\qquad (m,D)=1.
$$
有
$$
m\le aD^2+|b|D+c
\le D^{5/2}+D^{3/2}+D<2D^{5/2}.
$$

令
$$
\mathfrak a=(a,(-b+\sqrt{-D})/2),\qquad
\gamma=ax-(-b+\sqrt{-D})/2.
$$
则 $\gamma\in\mathfrak a$、$N\gamma=am$，所以
$$
\mathfrak b=(\gamma)/\mathfrak a
$$
是范数 $m$ 的整理想，其理想类为 $[\mathfrak a]^{-1}\ne1$。因为 $(m,D)=1$，没有分歧素理想；惰性素理想均为有理素数生成的主理想。因此 $\mathfrak b$ 至少有一个非主的分裂素理想因子 $\mathfrak q$。其范数就是有理素数 $q\le m$，证明 (58.20)。

取 $r=\operatorname{ord}[\mathfrak q]\le h$，由 (58.6)、(58.20) 即得 (58.7)。

最后给不隐藏常数的类数上界。二次虚域 Minkowski 界为
$$
B=\frac{2}{\pi}\sqrt D.
$$
每个理想类有范数不超过 $B$ 的整理想代表。范数为 $n$ 的整理想数不超过除数函数 $\tau(n)$：在分裂、惰性、分歧素数的各个素数幂处，计数分别为 $k+1$、至多 $1$、$1$。因此
$$
h\le\sum_{n\le B}\tau(n)
=\sum_{a\le B}\left\lfloor\frac Ba\right\rfloor
\le B(1+\log B).
$$
代入 (58.7) 便得到 (58.8)。

特别地，沿 $h_K>1$ 的实际异常序列，(58.8) 给出有效的渐近必要下界
$$
D_K\ \text{的绝对值}\ \gg
\frac{(\log p)^2}{(\log\log p)^4}.
$$
例如分成 $D\ge(\log p)^2$ 和 $D<(\log p)^2$ 两种情形，在后一种情形用 $\log D<2\log\log p$ 直接由 (58.8) 推出。这个下界与 $D$ 无界完全相容，不能反向读成绝对素数界。

## 8. 一个直接的全指数商域子范围排除

(58.6) 可在不计算完整类群的情况下使用。令 $r\in\{3,5,7\}$ 为素数，取正奇数 $u$ 使
$$
d=2^{r+2}-u^2>8
$$
平方自由。则 $d\equiv7\pmod8$，$K=\mathbb Q(\sqrt{-d})$ 的基本判别式为 $-d$，而 $2$ 分裂。元素
$$
\alpha=\frac{u+\sqrt{-d}}2
$$
的范数为 $2^r$。因 $\alpha+\bar\alpha=u$ 为奇数，其主理想只含 $2$ 上方两个素理想中的一个，故 $(\alpha)=\mathfrak q^r$。

$\mathfrak q$ 非主：范数为 $2$ 的元素会给 $x^2+dy^2=8$，在 $d>8$ 时无整数解。因此其阶恰为素数 $r$。有以下具体域：

| $r$ | $d$ |
|---:|---|
| $3$ | $23,31$ |
| $5$ | $47,79,103,119,127$ |
| $7$ | $71,151,223,287,391,431,463,487,503,511$ |

这些 $d$ 均平方自由；复合者为 $119=7\cdot17$、$287=7\cdot41$、$391=17\cdot23$、$511=7\cdot73$，其余素性可直接试除小于平方根的素数验证。

对这些域，(58.6) 给
$$
p<4\cdot2^{7/2}<46.
$$
而 $p>37$、$p\equiv1\pmod{12}$ 的素数至少为 $61$，矛盾。所以表中的十七个域在本同余类中对全部 $p>37$ 均不能作为实际商域。这不是对所有非类数一域的统一排除；表中也没有假定完整类数等于 $r$。

## 9. 输入、比较与未解决边界

- [R21](R21-twelfth-power-signature-and-cm-twists.md) 提供精确惯性型、循环自同构阶论证及 $2,3$ 的处理；本文额外使用 $p\equiv1\pmod{12}$ 将幂次降为 $2$。
- [R27](R27-fixed-quotient-field-at-one-mod-twelve.md) §4 提供 $p$ 处超奇异特殊纤维的自同构群为 $\{\pm1\}$。本文在 $q=2,3$ 处另证明了惯性特征延拓和二次扭曲的好约化，并非从 R27 的 $q\ge5$ 扭曲构造直接外推。
- 全局、局部互反映射与射线类群正合列可参见 J. S. Milne, *Class Field Theory*, v4.03 (2020), Chapter V，[作者原文](https://www.jmilne.org/math/CourseNotes/CFT.pdf)。本文已展开降到序类群的主理想条件及核上的同构，没有只由群阶相同推断分裂。
- Minkowski 界见 Milne, *Algebraic Number Theory*, v3.08 (2020), Theorem 4.3，[作者原文](https://www.jmilne.org/math/CourseNotes/ANT.pdf)。第 7 节其余估计均在文中证明。
- Momose 的有理 $p$ 同源定理不能直接用于 $E_K$：$C$ 在 $\mathbb F_p$ 上仍不可约。Larson–Vaintrob 的 associated-character 定理允许扩标量后的一维特征，可另作比较，但本文 (58.4)–(58.19) 的证明不依赖其未显式求值的例外集合；文献量词核验另见[本轮 associated-character 笔记](../notes/2026-11-12-associated-characters-and-varying-quotient-resume2.md)。

主要剩余问题仍是同时控制变化的 $K$ 与 $p$。(58.5) 可能自动满足，(58.6) 允许小素数理想类阶随 $p$ 增长，(58.8) 只迫使判别式增长。类数一的七个容许域也不由这些非主理想条件排除，仍有固定 CM 同余的最终整性缺口。

