# R118：环类数十二的实际三次周期非消失与分歧素数 Frobenius 约束

日期：2026-11-12；会话：serre-uniformity-resume2。

**状态：已证明，附完整严格整数证书。** 本篇完整处理环类数十二，不给素数 $p$ 预设搜索上限。先由原始导子、已发表无条件类数界与非零整数最大公因数列出六个实际候选；四个由同一真实 Frobenius 的十二次幂和三次角色排除，两个由商域分歧素数处的真实惯性与好约化迹排除。后一个局部引理不要求环类数十二，可独立复用。

## 1. 主定理与范围

设 $E/\mathbb Q$ 无 CM，$p>37$，且
$$
\operatorname{Im}\bar\rho_{E,p}=N_{\rm ns}(p),\qquad
\bar\rho_{E,p}(I_p)=C^3.
\tag{118.1}
$$
令 $K$ 为正规化子商二次域，$D=|D_K|$，选择 Cartan 特征
$$\lambda:G_K\longrightarrow\mathbb F_{p^2}^{\times}.$$
按 R66，
$$
\eta=\lambda^{(p^2-1)/3}
\tag{118.2}
$$
是准确导子 $c$ 的原始三阶环类角色，$p$ 在 $K$ 惰性，$p\nmid cD$，且
$$p\equiv2,5\pmod9.$$
记 $\mathcal O_c=\mathbb Z+c\mathcal O_K$、$M=Dc^2$，沿用 R76、R90 的素水平 Brandt 周期 $P_\eta$。

**定理 118.1。** 若 $h(\mathcal O_c)=12$，则
$$
\boxed{P_\eta\ne0.}
\tag{118.3}
$$
等价地，至少有一个层 $p$ 的权二新形式 $g$ 满足
$$
\boxed{L\bigl(\tfrac12,\pi_{g,K}\otimes\eta\bigr)\ne0.}
\tag{118.4}
$$

本定理不假设 $j(E)$ 整，也不预先限制坏素数支集。需要的是实际椭圆曲线的惯性与整数 Frobenius 迹；不能将结论扩张为任意抽象三阶环类角色、任意 $p\equiv2,5\bmod9$ 的非消失。

结合 R90、R113、R115，仍使全部这些三次中心值共同为零的实际小惯性分支必有
$$
\boxed{h(\mathcal O_c)\ge15.}
\tag{118.5}
$$
这里 $3\mid h(\mathcal O_c)$ 来自非平凡三阶角色。一般更大环类数、其他素数的 exceptional 分母和完整 Cartan 惯性并未由本篇解决。

## 2. 可复用的必要立方关系与原始性判据

### 2.1 任意环类数 $3m$ 的必要立方关系

设一个三阶环类角色 $\eta$ 的周期为零。选择 CM 椭圆曲线在 $p$ 的约化作为 Brandt 基准后，Deuring 对应将**右理想类**与超奇异椭圆曲线的同构类识别；环类群的可逆理想作用与约化相容。这里不是仅记录最大序的共轭类型。$p\nmid c$ 保持所需最优性，非极大序的 Tate 格接口与其他基准序之间的零周期传输已在 R80、R90 给出。

每个约化纤维中，设三种角色值的数量为 $n_0,n_1,n_2$。其周期系数为一个共同非零权重乘
$$n_0+n_1\zeta_3+n_2\zeta_3^2.$$
因 $1,\zeta_3$ 在 $\mathbb Q$ 上线性无关，此系数为零恰当 $n_0=n_1=n_2$。所以每个纤维的大小被三整除。对环类多项式
$$
H_{-M}(X)=\prod_{[\mathfrak a]\in\operatorname{Pic}(\mathcal O_c)}
\bigl(X-j(\mathfrak a)\bigr)\in\mathbb Z[X]
$$
得到
$$
\boxed{P_\eta=0\ \Longrightarrow\ H_{-M}(X)\bmod p=Q(X)^3,
\qquad Q\in\mathbb F_p[X]\text{ 首一},\quad\deg Q=m.}
\tag{118.6}
$$
首一立方根由根及其重数唯一决定，故被 Frobenius 保持。反向推论不成立：只有纤维大小被三整除并不能保证每个纤维三色平衡。本篇只使用 (118.6) 的必要方向。

由于 $\sum\eta=0$，周期位于次数零 Brandt 模。完整尖点特征谱及 Cai–Shu–Tian Theorem 1.2 的非零正归一化常数给
$$
P_\eta=0\quad\Longleftrightarrow\quad
L\bigl(\tfrac12,\pi_{g,K}\otimes\eta\bigr)=0
\text{ 对全部层 }p\text{ 的权二新形式 }g.
\tag{118.7}
$$
这沿用 R90 已核准的同一接口。

### 2.2 三阶 Sylow 子群阶为三时的准确原始性

令有限阿贝尔群 $G$ 满足 $v_3(|G|)=1$。则
$$G=G_{(3)}\times A,\qquad G_{(3)}\simeq C_3,\qquad 3\nmid|A|.$$
恰有两个三阶角色，互为逆，核均为 $A$。若 $G\twoheadrightarrow G'$ 满射，则此角色经 $G'$ 分解，当且仅当 $3\mid|G'|$：若目标阶被三整除，映射核的阶与三互素，因而包含于 $A$；若目标阶与三互素，则不存在非平凡三阶角色。

将其用于 $\operatorname{Pic}(\mathcal O_c)\twoheadrightarrow\operatorname{Pic}(\mathcal O_{c'})$，其中 $c'\mid c$，得到
$$
\boxed{v_3(h(\mathcal O_c))=1\ \Longrightarrow\
\eta\text{ 原始}\ \Longleftrightarrow\
3\nmid h(\mathcal O_{c'})\text{ 对每个真因子 }c'\mid c.}
\tag{118.8}
$$
此证明不要求整个类群循环。环类数十二时，类群可以是 $C_{12}$ 或 $C_6\times C_2$，二者的三次角色核都是完整的二主部分，阶为四。特别，对任一类 $x$，
$$
\boxed{\eta(x)=1\quad\Longleftrightarrow\quad x^4=1.}
\tag{118.9}
$$
这与 R115 的环类数九情形不同；这里的三主部分确实只有阶三。

## 3. 全部二百八十六个原始序的完整覆盖

理想扩张给 $h_K\mid12$。若 $h_K=3$ 或 $6$，则 $c>1$ 且角色已经由 (118.8) 降到 $c=1$，不原始；若 $h_K=12$，同样只能 $c=1$。所以只须枚举 $h_K=1,2,4,12$。

Watkins 已发表的无条件完全分类给：

| $h_K$ | 域的数量 | $D$ 的最大值 |
|---:|---:|---:|
| 1 | 9 | 163 |
| 2 | 18 | 427 |
| 4 | 54 | 1555 |
| 12 | 206 | 17803 |

作者 PDF 第23页的末表直接列出这些数值。验证器在这些已证明的全局界内重新枚举全部基本判别式及 primitive 正定约化二元型，不以经验上限或数据库清单代替完备性。

若 $c>1$，写 $u_K=[\mathcal O_K^\times:\{\pm1\}]\in\{1,2,3\}$，则
$$
12=\frac{h_Kc}{u_K}\prod_{q\mid c}\left(1-\frac{\chi_K(q)}q\right).
\tag{118.10}
$$
因此 $\varphi(c)\le12u_K/h_K\le36$。又
$$
\frac{\varphi(c)^2}{c}
=\prod_{q^e\parallel c}q^{e-2}(q-1)^2\ge\frac12,
$$
因为唯一可能小于一的局部因子是 $q=2,e=1$。所以
$$\boxed{c\le2592.}\tag{118.11}$$
枚举全部 $c$ 并应用准确判据 (118.8)，结果为

| $h_K$ | 原始序的数量 |
|---:|---:|
| 1 | 15 |
| 2 | 17 |
| 4 | 48 |
| 12 | 206 |
| 合计 | 286 |

最大 $M$ 为 $19723=163\cdot11^2$。每个域、导子、约化型及环类数公式核对均存入完整证书。

## 4. 非零整数最大公因数覆盖全部素数

下面的构造适用于任意首一 $H\in\mathbb Z[X]$，次数 $3m$。从最高次开始，递归唯一确定
$$Q=X^m+u_1X^{m-1}+\cdots+u_m\in\mathbb Z[1/3][X]$$
使 $Q^3$ 与 $H$ 的最高 $m+1$ 个系数相同。每一步新系数以 $3u_j$ 线性出现；其余项只依赖前面的 $u_i$。对余下 $2m$ 个系数，令
$$B_i=\operatorname{num}\bigl([X^i](H-Q^3)\bigr),\qquad
G_H=\gcd_{0\le i<2m}B_i.$$
全部分母都是三的幂。因此
$$
\boxed{p>3:\qquad H\bmod p\text{ 为首一式的立方}
\quad\Longleftrightarrow\quad p\mid G_H.}
\tag{118.12}
$$
对 $H=H_{-M}$，必有 $G_H>0$：若所有余项为零，特征零的类多项式就是立方，违反不同复 CM 理想类给不同 $j$ 的可分性。

本篇 $m=4$，所以有八个准确整数余项。各 $H_{-M}$ 通过其十二个约化型计算
$$
H_{-M}(X)=\prod_{[a,b,d]}
\left(X-j\left(\frac{-b+i\sqrt M}{2a}\right)\right).
$$
8192 位 Arb 复数球包住全部系数；每个系数的实部球含唯一整数且半径小于 $2^{-200}$，虚部球含零且绝对值上界小于 $2^{-200}$。CM 整性保证所隔离的整数就是准确系数。随后只用有理数和整数运算构造 $Q$、八个余项及 $G_H$。

程序对不超过一千的素数作精确试除，并断言最后余因子恰为一。因此所有素因子已经完全覆盖，实际最大素因子为 $317$。这个试除范围不是对未知素数 $p$ 的搜索截断；完备性来自最终余因子为一。

在全部 $286$ 个序上，保留 $p>37$、$p\nmid M$、$\chi_K(p)=-1$，共有四十个立方化候选对；完整表及各首一四次立方根在证书中。再保留实际小惯性条件 $p\equiv2,5\bmod9$，恰剩

| $M$ | $D$ | $c$ | $p$ | 排除接口 |
|---:|---:|---:|---:|---|
| 3048 | 3048 | 1 | 41 | 分歧素数 $127$ 的 Frobenius 平方条件 |
| 3820 | 955 | 2 | 41 | 分裂素数 $47$ 的同一迹与三次角色 |
| 4168 | 4168 | 1 | 47 | 分裂素数 $11$ 的十二次幂迹 |
| 4947 | 4947 | 1 | 41 | 分裂素数 $7$ 的同一迹与三次角色 |
| 10795 | 10795 | 1 | 59 | 分歧素数 $5$ 的真实好约化迹 |
| 11707 | 11707 | 1 | 317 | 分裂素数 $7$ 的十二次幂迹 |

程序还独立以模 $p$ 多项式乘法核对全部四十个 $Q^3$。下一节及第六节排除上表六行，均使用实际曲线的必要条件。

## 5. 四个分裂素数处的实际角色排除

置 $\mu=\lambda^{12}$。R63 给 $p$ 外不分歧及适当统一取向下的主理想公式
$$\mu((\alpha))=\widetilde\alpha^{12}.$$
取在 $K$ 分裂且 $q\not\equiv1\pmod p$ 的 $q\ge5$。潜在乘法已由 R2 排除。R63 的有限惯性忠实性、Frobenius 交换及连续截面论证给一个全分歧好约化扩张，剩余域仍为 $\mathbb F_q$，故有真实整数迹 $a$ 和 Cartan 根 $\beta$，满足
$$
|a|\le2\sqrt q,\qquad \beta+\beta^p\equiv a,\qquad
\beta^{p+1}=q,\qquad \beta^{12}=\mu(\mathfrak q).
\tag{118.13}
$$
若 $\mathfrak q^r=(\alpha)$、$\alpha=(T+Y\sqrt{-D})/2$，则
$$
T^2+DY^2=4q^r,\qquad \beta^{12r}=\widetilde\alpha^{12}.
$$
使用整数递推
$$S_0(t,n)=2,\quad S_1(t,n)=t,\quad
S_{j+1}(t,n)=tS_j(t,n)-nS_{j-1}(t,n)$$
得到必要条件
$$
\boxed{S_{12r}(a,q)\equiv S_{12}(T,q^r)\pmod p.}
\tag{118.14}
$$
以下每个 $\alpha$ 都是代数整数，范数式和 $\gcd(T,Y,q)=1$ 均精确验证，故其理想只支持 $q$ 的一个分支。

| $D,c,p$ | $q$ | $r$ | $T$ | $Y$ | (118.14) 后的全部整数迹 |
|---|---:|---:|---:|---:|---|
| $955,2,41$ | 47 | 4 | 1362 | 136 | $\pm12,\pm13$ |
| $4168,1,47$ | 11 | 3 | 34 | 1 | 无 |
| $4947,1,41$ | 7 | 6 | 589 | 5 | $0$ |
| $11707,1,317$ | 7 | 12 | 192771 | 1247 | 无 |

两个直接无迹的计算很短：

- 对 $D=4168,p=47,q=11$，右边为 $44$；$a=0,\ldots,6$ 的左边依次为
  $$21,6,38,33,3,35,3.$$
- 对 $D=11707,p=317,q=7$，右边为 $206$；$a=0,\ldots,5$ 的左边依次为
  $$69,23,113,13,23,23.$$

指数 $12r$ 为偶数，故负迹已同时覆盖。

### 5.1 $D=955,c=2,p=41$

此时
$$\alpha=681+68\sqrt{-955}\in\mathcal O_2,\qquad N\alpha=47^4.$$
纯支范数关系在 $\mathcal O_2$ 中说明 $[\mathfrak q]^4=1$，所以 (118.9) 给 $\eta(\mathfrak q)=1$。

另一方面，在 $\mathbb F_{41^2}=\mathbb F_{41}[s]/(s^2+955)$ 中，对表中全部 $a=\pm12,\pm13$ 同时解
$$2x=a,\qquad x^2+955y^2=47,\qquad\beta=x+ys.$$
恰有八个根。它们的三次角色值全部为
$$\beta^{560}\in\{20+10s,\ 20+31s\},$$
均不为一。这与同一个实际 $\eta(\mathfrak q)$ 矛盾。

这里没有把两条不同局部曲线的迹和角色拼在一起：$\eta$ 在 $q\nmid c$ 不分歧，全分歧好约化扩张保留该 Frobenius 的角色值。

### 5.2 $D=4947,c=1,p=41$

若 $[\mathfrak q]^4=1$，则应有纯支生成元，满足
$$U^2+4947V^2=4\cdot7^4=9604.$$
只可能 $V=0,\pm1$。$V=0$ 给 $U=\pm98$，生成元为有理数 $\pm49$，同时使用 $7$ 的两支；$|V|=1$ 给 $U^2=4657$，不是平方。因此 $[\mathfrak q]^4\ne1$，由 (118.9) 得 $\eta(\mathfrak q)\ne1$。

但 (118.14) 只允许 $a=0$。在 $s^2=-4947$ 的 $\mathbb F_{41^2}$ 中，范数七且迹零的两根恰为 $15s,26s$，二者均满足 $\beta^{560}=1$，再次矛盾。

至此上表四个分裂素数候选全部排除。

## 6. 商域的分歧素数给更强的真实局部限制

以下引理不要求小惯性、不要求三次角色，也不要求 $j(E)$ 整。

**引理 118.2。** 设 $E/\mathbb Q$ 的模 $p$ 像包含于非分裂 Cartan 正规化子，$p>37$，商二次域为 $K$。若素数 $q\ge5$、$q\ne p$ 在 $K$ 分歧，则：

1. $E$ 在 $q$ 潜在好约化，有限惯性像恰为外陪集元素生成的 $C_4$。
2. 若 $q\equiv1\pmod4$，则 $(q/p)=1$，并且存在真实整数 $a$ 满足
   $$|a|\le2\sqrt q,\qquad a^2\equiv4q\pmod p.$$
   特别
   $$\boxed{p\le4q.}\tag{118.15}$$
3. 若 $q\equiv3\pmod4$，则
   $$\boxed{\left(\frac{-q}{p}\right)=-1.}\tag{118.16}$$
4. 在两种情况下，对 $G_{K_q}$ 的 Frobenius $g$ 都有
   $$\lambda(g)^4=q^2.$$
   此值与惯性提升无关；它是局部不分歧角色 $\lambda^4$ 在该素理想的值。

**证明。** 若 $E$ 潜在乘法，R2 说明剩余惯性像由标量 $\pm I$ 组成，商角色在惯性上平凡，与 $q$ 在 $K$ 分歧矛盾。因此 $E$ 潜在好约化。

因 $q\ge5$，有限惯性温和循环，阶属于 $\{1,2,3,4,6\}$。它在模 $p$ 表示中忠实：其阶与 $p$ 互素，而 $\operatorname{GL}_2(\mathbb Z_p)$ 的模 $p$ 约化核是 pro-$p$。取投影到正规化子商非平凡的惯性元素 $\tau$。行列式在 $q\ne p$ 的惯性上为一，外陪集元素的迹为零，所以
$$\bar\rho(\tau)^2=-I.$$
这强迫惯性阶为四，其生成元位于外陪集。

因为 $K_q/\mathbb Q_q$ 分歧二次，可以选择一个算术 Frobenius 提升 $g\in G_{K_q}$：从任意提升出发，必要时乘以 $\tau$，并不改变它在非分歧商上的像。记 $b=\lambda(g)$，则 $b^{p+1}=q$。温和关系为
$$g\tau g^{-1}=\tau^q$$
（先在有限惯性商中理解）。Cartan 元素与一个外陪集生成元的共轭关系给
$$
b/b^p=
\begin{cases}
1,&q\equiv1\pmod4,\\
-1,&q\equiv3\pmod4.
\end{cases}
\tag{118.17}
$$
前一情形 $b\in\mathbb F_p^\times$，故 $b^2=q$；后一情形 $b^p=-b$ 且 $b\notin\mathbb F_p$，故 $b^2=-q$，并且 $-q$ 必为模 $p$ 非平方。这已给平方条件及 $b^4=q^2$。

还需在 $q\equiv1\bmod4$ 情形得到**真实整数迹**，不能只用 $b^2=q$。令
$$N=\ker\bigl(\rho_{E,p^\infty}|_{I_q}\bigr),\qquad \Gamma=G_{\mathbb Q_q}/N.$$
这是有限惯性 $I\simeq C_4$ 对 $\widehat{\mathbb Z}$ 的扩张。有限惯性模 $p$ 忠实，故 $g$ 与 $I$ 的剩余交换关系提升为 $p$ 进交换关系；等价地，温和关系中的 $q\equiv1\bmod4$ 已使此作用平凡。

由 $g$ 定义的连续同态 $\widehat{\mathbb Z}\to\Gamma$ 将 $1$ 送到 $g$，与非分歧投影复合为恒等映射。因此其像 $H=\overline{\langle g\rangle}$ 与 $I$ 交于一，投影到 $\widehat{\mathbb Z}$ 同构。$H$ 是指数四的开子群；因它与 $I$ 交换，还为正规子群。将其拉回绝对 Galois 群，固定域为循环全分歧四次扩张 $L/\mathbb Q_q$，剩余域仍为 $\mathbb F_q$。

$I_L$ 落在 $N$，所以 Néron–Ogg–Shafarevich 判据给 $E/L$ 好约化。该特殊纤维的 Frobenius 是所选 $g$，有整数迹 $a$、$|a|\le2\sqrt q$。其模 $p$ 矩阵是标量 $bI$，所以 $a\equiv2b$、$a^2\equiv4q\pmod p$。

由于素数 $q$ 不是平方，整数 $a$ 不可能使 $a^2=4q$，故
$$0<4q-a^2\le4q.$$
若 $p>4q$，这个严格正整数不可能被 $p$ 整除，证明 (118.15)。最后，限制到 $G_{K_q}$ 的惯性为 $\{\pm I\}$，四次幂消去；改变 Frobenius 提升不改变 $\lambda(g)^4$。证毕。

### 6.1 排除 $D=3048,p=41$

$127\mid3048$，且 $127\equiv3\pmod4$。但
$$-127\equiv37\equiv18^2\pmod{41}.$$
这违反 (118.16)，故该候选不可能来自实际椭圆曲线。

### 6.2 排除 $D=10795,p=59$

$5\mid10795$，且 $5\equiv1\pmod4$。引理强迫 $p\le4\cdot5=20$，与 $p=59$ 矛盾。也可直接看：真实迹只能为 $-4,\ldots,4$，其中没有 $a^2\equiv20\pmod{59}$ 的解。

至此第 4 节全部六个候选均已排除，由 (118.6)、(118.7) 证明定理 118.1。

## 7. 严格证书、独立核验与复算

- [完整验证器](../scripts/verify_class_number_twelve_periods.py)：重新枚举全部原始序，严格隔离十二次类多项式，重新构造八个有理余项，完整分解其整数 gcd，并检验六个实际局部矛盾。
- [完整压缩整数证书](../scripts/data/class_number_twelve_periods.json.gz)：保存全部二次域、导子、约化型、准确系数、有理四次根、八个余项、完整素数幂分解、四十个立方化候选及全部实际局部根。
- [独立 PARI/GP 多项式算法](../scripts/class_number_twelve_polynomials.gp)：另算全部二百八十六个类多项式，逐系数与严格 Arb 隔离整数比较。

复算：

~~~sh
python3 -B topics/serre-uniformity/scripts/verify_class_number_twelve_periods.py
gp -q -s 536870912 topics/serre-uniformity/scripts/class_number_twelve_polynomials.gp
~~~

验证器已经通过全部 $286$ 个严格系数和完整因子分解，以及六个实际局部排除。压缩证书为 **1125443 字节**，解压后 JSON 为 **2525939 字节**，压缩文件 SHA256 为

~~~text
f46681982da8edd0d29b4de741858e39e44823d46e378a9691215ba7a578fc54
~~~

另以 PARI/GP 2.19.0 的 `polclass` 独立算完全部 $286$ 个多项式，与 Arb 隔离整数逐系数比较，**286/286 全部相同**。该 JSON 行输出的 SHA256 为

~~~text
2ad88f2f4ac2302f28a2ce38839423480355753c0a4ee71ba6ee9ed4dcf2b768
~~~

验证器依赖 python-flint/Arb；有限域、范数、迹递推、整数分解和覆盖检查均为精确算术。PARI 对照只提供独立算法复核，不承担严格系数隔离或全局完备性。

## 8. 原始来源

1. M. Watkins, *Class numbers of imaginary quadratic fields*, Mathematics of Computation **73** (2004), no. 246, 907–938，DOI [10.1090/S0025-5718-03-01517-5](https://doi.org/10.1090/S0025-5718-03-01517-5)；[作者全文](https://magma.maths.usyd.edu.au/~watkins/papers/smallcn.pdf)，第23页末表列出 $h_K=1,2,4,12$ 的完整数量与最大判别式。其有限清单在本篇全部重新枚举。
2. L. Cai, J. Shu, Y. Tian, *Explicit Gross–Zagier and Waldspurger formulae*, Algebra & Number Theory **8** (2014), 2523–2572，[期刊全文](https://msp.org/ant/2014/8-10/ant-v8-n10-p05-p.pdf)，Theorem 1.2；[R90 §2](R90-class-number-three-periods-and-actual-frobenius-exclusions.md) 已核所用的完整 Brandt 周期等价。
3. J. Voight, *Quaternion Algebras*, Springer, 2021，[第42章](https://link.springer.com/chapter/10.1007/978-3-030-56694-4_42)：右理想类、超奇异椭圆曲线和 Deuring 对应；非极大序及基准序传输沿用 R80、R90。
4. [R21](R21-twelfth-power-signature-and-cm-twists.md)、[R63](R63-all-prime-classes-and-quotient-discriminant-growth.md)：有限惯性忠实性、主理想公式、连续 Frobenius 截面和真正的好约化迹；第 6 节给出分歧商域的独立局部推导。
5. [R66](R66-cubic-conductor-nonvanishing-and-tate-primes.md)：原始三次角色及实际 $p\equiv2,5\bmod9$；[R113](R113-class-number-six-cubic-period-nonvanishing.md)、[R115](R115-class-number-nine-periods-and-actual-trace-exclusion.md)：已处理的更小环类数分支。
6. [FLINT 模函数文档](https://flintlib.org/doc/acb_modular/index.html)及 [python-flint 复数球](https://python-flint.readthedocs.io/en/latest/acb.html)：本篇使用的严格模函数包围与唯一整数隔离接口。
