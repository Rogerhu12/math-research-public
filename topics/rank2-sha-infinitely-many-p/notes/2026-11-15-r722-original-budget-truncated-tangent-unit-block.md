# R722 增补：截掉顶 charge 后的原同 D 单位块

日期：2026-11-15。**状态：已证明。**
本增补把 R722 的核收紧真正放回旧预算，
不要求把原矩阵扩大到 $D+2$ 或 $D+3$。
代价是删去两个或三个明确的高 charge 来源块，只有线性数量的列。

## 1. 精确截源和全部原帽

保持 R722 的同一个 $F,Q,P^{\rm fact}$ 和 $D_0=3b+\deg_YQ\le D$。
取 $j=2$ 或 $3$，分别使用该篇的 $\mathcal T_2$ 或 $\mathcal T_3$。
定义
$$
\boxed{
\mathcal H_2^{\le 2b-j}
=\{H\in\mathcal H_2:\deg_YH\le2b-j\}.
}
\tag{1}
$$
它是原逐 charge 整基的直和因子。
R517/R521 的全部十九角返回证明与 $Y$ 次数上界相互独立；
对 (1)，
$$
\deg_Y\mathcal V_FH\le b+(2b-j)=3b-j.
$$
乘原 $j$ charge 清极量后总次数至多 $3b$。
再乘同一个 $Q,d^{-C_D},t^r$，因此
$$
\boxed{
\mathcal T_j(\mathcal H_2^{\le2b-j})\subset\mathcal W_{D_0}
\subset\mathcal W_D
}
\tag{2}
$$
整成立。有限角、无穷远、原允许分母和每一个中间角全按旧证明保留。
这只用原双向 Gauss 判据在更小的实际 $Y$ 次数上读取；
没有把较大矩形并入 $\mathcal W_D$。

注意
$$
kF^2\cap\overline{\mathcal H}_2^{\le2b-j}=0
\tag{3}
$$
因为 $\deg_YF^2=2b$，其最高系数非零。

## 2. 原低角保证实际二 jet 分裂

令
$$
i_0=\min\{i:\bar f_i(0)\ne0\},
\qquad F=\sum_{i=0}^bf_i(t)Y^i.
$$
$F(P)=0$、$(\mathcal EF)(P)\ne0$ 保这个集合非空，
且至少有两个元素。

原 $0$ 角的权为 $(4,-1)$。
由于 $Q(P)$ 为单位，$v_0(Q)\le0$。
$P^{\rm fact}\in\mathcal W_D$ 给
$$
4r+v_0(Q)+3v_0(F)\ge-2,
$$
从而
$$
v_0(F)\ge-\frac{4r+2}{3}.
$$
每个 $\bar f_i(0)\ne0$ 的真实项都满足
$-i\ge v_0(F)$。所以
$$
\boxed{
i_0\le\left\lfloor\frac{4r+2}{3}\right\rfloor-1.
}
\tag{4}
$$
最后少一来自至少两个互异 charge，不是另加稀疏性假设。

每个单独的 $f_i(t)Y^i$ 仍在原 $\mathcal H_1$：
该格的原 ambient 帽和全部十九角条件按 charge 系数分别给出。
取同一整点 $\widetilde P$，置
$$
U=\frac{f_{i_0}(t)Y^{i_0}}
{f_{i_0}(0)\widetilde\psi(0)^{i_0}}
\in\mathcal H_1,\qquad U(\widetilde P)=1.
\tag{5}
$$
分母是单位，且 $\mathcal EU=i_0U$。

如果
$$
\boxed{b\ge i_0+j,}
\tag{6}
$$
则 $FU$ 和 $U^2$ 都属于 (1)。
相应准确整二 jet 截面是
$$
H^{(1)}=FU,\qquad
H^{(0)}=U^2-\frac{2i_0}{e_0}FU,\qquad
e_0=(\mathcal EF)(\widetilde P).
\tag{7}
$$
它们在
$(H(\widetilde P),(\mathcal EH)(\widetilde P)/e_0)$
上分别取 $(0,1),(1,0)$。

只用原参数的充分门由 (4) 给出：
$$
\boxed{
b\ge\left\lfloor\frac{4r+2}{3}\right\rfloor+j-1.
}
\tag{8}
$$
特别，对两 charge 返回，$r=1$ 时 $b\ge3$ 足够，
$r=2$ 时 $b\ge4$ 足够。
实际 $i_0$ 更小时应使用较强的 (6)。

## 3. 不含 F² 的原同预算单位块

令
$$
\mathcal H_{\rm cut}^{00}
=\{H\in\mathcal H_2^{\le2b-j}:
H(\widetilde P)=(\mathcal EH)(\widetilde P)=0\}.
\tag{9}
$$
由 (7)，这是原有限自由直和因子，余维准确为二。

继续保 R722 的
$$
T_J=s-r-1\quad\text{或}\quad T_M=s-r-14,
\qquad T>2\kappa,\quad h>\kappa .
\tag{10}
$$
R722 的真实核证明说：任何 (9) 中的约化物理核都在 $kF^2$。
再由 (3)，这个核只能为零。
所以：

**定理。** 同一旧 $\mathcal W_D$ 中的整矩阵
$$
\boxed{
(J\text{ 或 }M)\,\mathcal T_j:
\mathcal H_{\rm cut}^{00}\longrightarrow\mathscr T
}
\tag{11}
$$
是分裂整单射，全部 Smith 因子为单位。
这里不再商掉 $F^2$，也没有扩大来源预算。

写原 R517 的真实系数格为
$$
\mathcal H_2=\bigoplus_{i=0}^{2b}
Y^iD_i(t)\mathcal O[t]_{\le m_i}
$$
并令
$$
\delta_j=\sum_{i=2b-j+1}^{2b}(m_i+1)_+ .
$$
则 (11) 的秩准确为
$$
\boxed{
1+2\kappa+\chi-\delta_j-2
=2\kappa+\chi-1-\delta_j.
}
\tag{12}
$$
原 ambient 帽给 $m_i\le2u+4i$，故
$$
0\le\delta_j\le j(2u+8b+1).
\tag{13}
$$
这是一个线性损失；实际应用优先用 (12) 的准确整数。
在满主阶 $u=b+O(1)$ 时，
(11) 的真实同预算单位块仍有
$47b^2/6+O(b)$ 个单位因子。

## 4. 截源的两条残余列仍准确给定

用 (11) 的整商后，
整个截源 (1) 的像只再增加 (7) 的两条实际列。
它们的来源准确为
$$
\boxed{
\begin{aligned}
\mathcal T_j(H^{(1)})
&=c_{\rm src}F\,\mathcal V_FU,\\
\mathcal T_j(H^{(0)})
&=c_{\rm src}
\left(2U-\frac{2i_0}{e_0}F\right)\mathcal V_FU,
\end{aligned}}
\tag{14}
$$
其中
$$
\mathcal V_FU
=\frac{Y^{i_0}}{f_{i_0}(0)\widetilde\psi(0)^{i_0}}
\bigl(e\,t f_{i_0}'-i_0a_0f_{i_0}\bigr).
\tag{15}
$$
(15) 是原多项式，不引入 $f_{i_0}$ 的新分母。

在 (10) 下，整个截源的物理核准确单射到这两条原点坐标中，
故其维数至多二。
$Z=0$ 时，$1,F$ 均在截源且给满两坐标，
所以该截源的全部实际像已是 (11) 的单位块。
$Z>0$ 时，来源核本身为零；
至多两个来源方向仍可有非单位或额外物理零因子。
这些方向的准确值由 (14) 的整矩阵决定。

### 4.1 额外方向必须给更高 t 阶的真原首核

令 $\mathsf M_0$ 为所选原 $J$ 或完整原 $M$，
令 $I_{\rm cut}$ 为截源的真实物理核在两原点坐标中的像。
在 $Z>0$ 时，R537 的来源核为 $kF^2$，
而 (3) 已将它全部截掉，所以
$\overline{\mathcal T_j}$ 在该截源上单射。
它把 $I_{\rm cut}$ 准确送入
$$
\ker\overline{\mathsf M}_0
\cap t^{r+1}k[t,Y,d^{-1}].
$$
另一方面，$Q(P)$ 为单位、$F$ 不被 $t$ 整除，
故 $P^{\rm fact}$ 的公共 $t$ 阶恰为 $r$。
因此这一整片真核与 $k\bar P^{\rm fact}$ 直和，得到
$$
\boxed{
\dim_k\ker\overline{\mathsf M}_0\ge1+\dim I_{\rm cut}.
}
\tag{16}
$$
特别，若实际已经证明
$\ker\bar J=k\bar P^{\rm fact}$，
则 $I_{\rm cut}=0$，
截源的两条残余列也有完整单位秩；
此时整个截源的相对物理像都是饱和的。
对只知 $\ker\bar M$ 的情形使用其对应版本，
不能将两种核互换。

(16) 是实际核维数的条件推论，
不声称当前原首核已经一维，也不限制未知修正 $R$ 的奇偶性。

## 5. 与指定乘后 forcing 的接口

在
[指定极端 forcing 增补](2026-11-15-r722-specified-extreme-forcing-outside-unit-block.md)
的 (6) 窗口，原乘后目标不在 (11) 的像中。
因为 (11) 的来源是 R722 的 $\mathcal H_2^{00}$ 的实际子格，
该增补的同一个矛盾证明直接适用。
这次若 (6)/(8) 成立，单位块确实属于旧 $\mathcal W_D$，
不再附带扩大 $D+2$ 的范围。

它仍可能被 (14) 的两列与其余真正 $\mathcal W_D$ 列共同吸收。
完整首位、同一个首次修正 $R$、两条十三行 carry 和第三位
继续在同一个整商中计算；没有把两个单独子像的非吸收相加成全像非零。
