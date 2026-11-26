# R150 附录：单位 2+1+1 相反配对一般 mean 图的六条异常曲线全部排除

作者：Astra-ISP-347c-20261126 / unit31_general；AI-assisted GPT-6 Astra Pro。日期：2026-11-26 UTC。

**状态：本条精确范围已证明。** 保留原单位 $2+1+1$ 加孤立零点分支，令 $p=1,q=-1,u=b-c\ne0$。在已支付全部奇异面的 $D_1D_2\ne0$ 原 mean 图中，本条排除
$$
v\,w\,(v+w)\,B\,G_-\,G_+=0,
$$
其中各因子定义见下文。它们正是下一轮低次结式移去之前必须完整支付的曲线。本条不以这些边界排除宣称整个一般图或 ISP 已解决。

## 1. 原 Cramer 图与允许除去的精确因子

完全沿用[两个奇异 mean 图专条](R150-appendix-essential-four-unit-two-plus-one-plus-one-opposite-base-pairings-singular-mean-charts-exclusion.md)的同一原长度五除子 $2A+B+C+Z$、原六维非退化配对、Frobenius 单位代数、原 mean $E$、原最高式 $P$、第二梯度 $N$ 和全部值、一阶 jet。参数为
$$
\ell=b+c,\quad u=b-c,\quad e=u^2,\quad
a=1-\ell,\quad b=(\ell+u)/2,\quad c=(\ell-u)/2,
$$
$$
X=(d_B+d_C)/2,\quad v=d_B-d_C-1,\quad w=ut,\quad T=uX.
$$
原 $E_0=0$ 给
$$
f=X/2+u/2+\ell v/(4u),
$$
而 $r,s,A_1$ 按前稿 (1.2) 完整恢复，未改变原物理 Gram。定义
$$
B=v^2+vw-w+1,\quad D_1=-2\ell+v-w+1,
\quad D_2=-2\ell(v+1)+B.
$$
原 $E_+,E_-$ 对 $(T,e)$ 的线性系数行列式为 $-2D_1D_2$。在本图，Cramer 公式精确为
$$
e_*=
\frac{\ell\bigl(\ell v^3-\ell v^2-\ell vw^2-\ell w^2+w^2\bigr)}{D_1D_2},
$$
$$
T_*=e_*+\frac{\ell(v-1)(v+w)-w^2}{2D_1}.                       \tag{1.1}
$$
再定义
$$
H=-2\ell^2(v+1)+\ell(2v^2+v-2w+1)-w^2.
$$
原身份为
$$
e_*-\ell^2=\frac{\ell(2\ell-1)H}{D_1D_2}.                    \tag{1.2}
$$
原 Frobenius 条件为 $e\ne0,e\ne\ell^2$。完整的[$\ell=0$ 排除](R150-appendix-essential-four-unit-two-plus-one-plus-one-opposite-base-pairings-zero-total-weight-exclusion.md)、[$\ell=1/2$ 排除](R150-appendix-essential-four-unit-two-plus-one-plus-one-opposite-base-pairings-half-total-weight-exclusion.md)和[全部 $D_1D_2=0$ 排除](R150-appendix-essential-four-unit-two-plus-one-plus-one-opposite-base-pairings-singular-mean-charts-exclusion.md)已分别支付，所以本图必有
$$
\ell(2\ell-1)D_1D_2\,\operatorname{num}(e_*)\,H\ne0.           \tag{1.3}
$$

继续保留原剩余 mean $M=u^2E_1$ 与由原零点 mean、最高式、第二梯度得到的
$$
S=\overline P-2\overline N=0,\qquad
c_0=3P_0N_1-2N_0P_1=0.                                      \tag{1.4}
$$
其中 $\overline P=aP_0+P_1+bP_B+cP_C$，$\overline N$ 同理。$M,S/u,c_0$ 都是 $u$ 的偶有理式，故用 $e=u^2$ 表示。以下一律把 (1.1) 代入这三个原有理式。

为使所有因子账目明确，记 $\operatorname{num}$ 为约去分子分母公因子后取分子；记 $\operatorname{Strip}(F,Q)$ 为反复以 $\gcd(F,Q)$ 精确除去所有公共的非常数因子。这里只允许 $Q$ 取 (1.3) 的乘积，或在指定纤维代入后各已知非零分子的乘积。因此 Strip 的每个除数都已证明非零，绝不选择一个看起来有用的因子代替原分子。以此得到一般图的多项式 $M_*,S_*,C_*$，关于 $(\ell,v,w)$ 的次数分别为
$$
(4,6,5),\quad(4,7,5),\quad(9,14,10).                         \tag{1.5}
$$
每个真正原解都必须使它们为零。下述各纤维亦按同一个明确定义直接从原式生成，故没有用这些必要条件反向制造物理临界点。

## 2. $v=0$ 与 $w=0$ 的完整纤维

### 2.1 $v=0$

原 $M,S/u$ 的化简分子在仅除去 (1.3) 非零因子后，分别是非零常数乘
$$
2\ell+w,\qquad -2\ell+w+2.
$$
所以 $w=-1,\ell=1/2$，与已经完整排除的半总权纤维矛盾。这支付 $v=0$ 全面。

### 2.2 $w=0$

此时原 Cramer 参数为
$$
e_*=
\frac{\ell^2v^2(v-1)}{(-2\ell+v+1)(-2\ell v-2\ell+v^2+1)},
$$
$$
T_*=
\frac{\ell v(v-1)(-2\ell+v^2+1)}
 {2(-2\ell+v+1)(-2\ell v-2\ell+v^2+1)}.
$$
因此 $v=0,1$ 都不允许。按第一节定义所得两个原多项式为非零常数乘
$$
M_w=(v-\ell)(v^2+1-2\ell),
$$
$$
S_w=2\ell^2+\ell v^2-2\ell v-3\ell+v^3-v^2+v+1.
$$
完整 $\ell$ 结式为非零常数乘
$$
v^2(v-1)^2(v+1)^2(2v-1).                                    \tag{2.1}
$$
只剩 $v=-1$ 或 $v=1/2$。$v=1/2$ 时两个多项式的精确 gcd 为非零常数乘 $\ell-1/2$，已排除。$v=-1$ 时 gcd 为非零常数乘 $\ell^2-1$，保留两个完整纤维：

- $\ell=-1$ 时，原 $e_*=-1/2,T_*=-1$，原 $c_0$ 精确等于 $27/4$，故不成立。
- $\ell=1$ 时，原 $e_*=1/2,T_*=0$，恢复原参数得到 $a=0,A_1=r=s=t=f=0$。原最高值和 jet 为 $P_0=-u/2\ne0$，$P_1=P_B=P_C=0$。

第二个纤维不能仅因部分抽象方程成立而被保留为临界点。原最高式给零点配对列 $U=(u_0,0,0,0)$ 且 $u_0\ne0$。此时完整五维 Gram 的 $B,C,Z$ 行互为倍数，一阶 jet 行为零，秩为二。原长度五 jets 独立，而非退化六维配对限制到五维空间的秩至少四，矛盾。因此 $w=0$ 整面也被排除。

## 3. $v+w=0$ 与 $B=0$ 的完整纤维

### 3.1 $v+w=0$

令 $w=-v$。原 Cramer 参数为
$$
e_* =\frac{\ell v^2}{(v+1)(-2\ell+2v+1)},\qquad
T_*=-\frac{v^2(-2\ell+v+1)}{2(v+1)(-2\ell+2v+1)}.
$$
由原 $M,S/u,c_0$ 构造三个分子并按 (1.3) 精确 Strip，分别记为 $M_o,S_o,C_o$。两个完整结式 $\operatorname{Res}_{\ell}(M_o,S_o)$、$\operatorname{Res}_{\ell}(M_o,C_o)$ 的精确 gcd 为非零常数乘
$$
v^3(v+1).
$$
$v=0$ 已排；$v=-1$ 使原 $D_2=(1-2\ell)(v+1)$ 为零，与本图假设矛盾。所以这条曲线为空。

### 3.2 $B=0$

$v=1$ 时 $B=2$，故必须 $v\ne1$ 且
$$
w_B=-\frac{v^2+1}{v-1}.                                     \tag{3.1}
$$
由原三式同样构造 $M_B,S_B,C_B$。两个完整 $\ell$ 结式的精确 gcd 为非零常数乘
$$
v^3(v-1)^{10}(v+1)(v^2+1)^4(2v^4+v^2+1)^4.                  \tag{3.2}
$$
$v=0,1$ 已排；$v=-1$ 时原 $D_2=-2\ell(v+1)+B=0$；$v^2+1=0$ 经 (3.1) 得 $w=0$，亦已完整排除。最后必须保留并处理
$$
F_4=2v^4+v^2+1=0.                                           \tag{3.3}
$$
在 $\mathbb Q[\ell,v]$ 上，将原 $M_B,S_B,C_B$ 分别对 $F_4$ 取余，并加入 $F_4$，得到的约化 lex Gröbner 基恰为
$$
L_2=\ell^2+\ell v^3+\ell v^2-\frac{\ell v}{2}-\frac\ell2
 -\frac{3v^3}{4}-\frac{v^2}{4}-\frac v8+\frac18,
\qquad F_4/2.                                                \tag{3.4}
$$
模 $F_4$ 有精确身份
$$
L_2=\left(\ell-\frac{v^2}{v-1}\right)^2,
\qquad D_1=-2\left(\ell-\frac{v^2}{v-1}\right).
$$
由于 $v-1\ne0$，(3.4) 在复数点上迫 $D_1=0$，违背原 Cramer 图。等价的完全多项式核验是 $\operatorname{num}(D_1|_{w=w_B})^2$ 对 (3.4) 约化为零。这里保留了四次候选全部根和重数，绝未把得到有限候选误写成已排除。

## 4. 两条三次曲线的分母商环排除

定义
$$
G_-=v^3-vw^2-vw+v-w^2-w,
\qquad
G_+=v^3-vw^2+vw-v-w^2-w.                                    \tag{4.1}
$$
在 $G_-=0$ 上 $v=-1$ 会给 $-2=0$；在 $G_+=0$ 上 $v=-1$ 会给 $-2w=0$，而 $w=0$ 已支付。所以两条曲线均有 $v+1\ne0$。这保证按 $w$ 对 $G_\pm$ 取余时，首项系数 $-(v+1)$ 非零。

把第一节 $M_*,S_*,C_*$ 分别对 $G_\pm$ 关于 $w$ 取余并清除这些已付分母。然后在对应商环中，以原非零 Cramer 分母作精确多项式除法：

| 曲线 | 除数 | 在 $M_*,S_*,C_*$ 中依次除去的重数 | 新多项式的 $\ell$ 次数 |
|---|---|---|---|
| $G_-=0$ | $D_2$ | $1,1,4$ | $3,3,5$ |
| $G_+=0$ | $D_1$ | $2,2,4$ | $2,2,5$ |

这里的精确含义是：每次以指定 $D_i$ 关于 $\ell$ 作除法，其余式对 $G_\pm$ 约化为零，才取商。$D_1$ 的 $\ell$ 首项系数是 $-2$，$D_2$ 的是 $-2(v+1)$；除此之外，只在 $G_\pm$ 取余时引入 $v+1$ 的幂。因此所有新增分母均已明确非零。每次只删除原 $D_i\ne0$ 的因子，未把必要方程改成任意选定的不可约因子。

分别记所得三式为 $M_\pm,S_\pm,C_\pm$。在 $\mathbb Q$ 上计算完整结式
$$
R_{\pm,S}(v)=\operatorname{Res}_w
 \bigl(\operatorname{Res}_{\ell}(M_\pm,S_\pm),G_\pm\bigr),
$$
$$
R_{\pm,C}(v)=\operatorname{Res}_w
 \bigl(\operatorname{Res}_{\ell}(M_\pm,C_\pm),G_\pm\bigr).
$$
精确结果为

| 曲线 | 两个结式的次数 | 精确 gcd，忽略非零常数 |
|---|---|---|
| $G_-=0$ | $93,145$ | $v^{25}(v+1)^{40}(v^2+1)^4$ |
| $G_+=0$ | $67,146$ | $v^{17}(v-1)^6(v+1)^{31}F_4$ |

这里只使用共同有限根必使结式为零这一必要方向。首项下降造成的额外根没有删除，均在下一节按原式保留回代。

## 5. 三次曲线剩余纤维在原 Cramer 分母上矛盾

### 5.1 $G_-$ 的二次纤维

由第四节及已付 $v=0,-1$，只剩 $v^2+1=0$。原 $G_-$ 此时变成 $-(v+1)w(w+1)$，所以 $w=0$ 或 $-1$。前者已经完整排除。

对 $w=-1$，直接把第一节的原 $M_*,S_*,C_*$ 代入并对 $v^2+1$ 取余，加入 $v^2+1$ 后的精确约化 Gröbner 基为
$$
\{\ell+v/2,\ v^2+1\}.                                      \tag{5.1}
$$
于是原 $D_2=0$，矛盾。源码亦验证 $D_2^2$ 对 (5.1) 的多项式余式为零，未通过除以某个可能为零的量排除此纤维。

### 5.2 $G_+$ 的四次纤维

除了已排的 $v=0,-1$，第四节还给 $v=1$ 或 $F_4=0$。$v=1$ 使原 $G_+=-2w^2$，进而 $w=0$，已排。

在 $F_4=0$ 上，保留所有四个 $v$ 根。$v\pm1$ 均非零，原三次曲线有精确分解
$$
G_+=-(v+1)(w-w_B)(w-w_O)\pmod {F_4},
$$
$$
w_B=-\frac{v^2+1}{v-1},\qquad
w_O=\frac{v-1}{v+1}-w_B\equiv-2v^2+v-1\pmod {F_4}.           \tag{5.2}
$$
第一根已经由完整 $B=0$ 专节排除，故只须代回第二根。直接将原 $M_*,S_*,C_*$ 代入 $w=w_O$，按 $F_4$ 取余并加入 $F_4$，其精确约化 Gröbner 基为
$$
\left\{\ell^2-2\ell v^2-2\ell+\frac{3v^2}{2}+\frac12,
\quad F_4/2\right\}.                                        \tag{5.3}
$$
由 $F_4=0$，第一式恰为 $(\ell-v^2-1)^2$。而 (5.2) 给原 $D_1=-2(\ell-v^2-1)$，故 $D_1=0$，矛盾。完全多项式的核验同样是 $\operatorname{num}(D_1|_{w=w_O})^2$ 对 (5.3) 余式为零。

至此，六个因子的每一种零纤维、所有交点、所有新除数和两个四次重根候选都已支付。在真正剩余图中可以合法使用
$$
v\,w\,(v+w)\,B\,G_-\,G_+\ne0.                              \tag{5.4}
$$

## 6. 原式源码与结论范围

配套[自含 QQ 源](../notes/2026-11-26-unit211-opposite-regular-exceptional-curves-347c.py)从原 Frobenius 乘法、原 Gram、mean、最高值及 jet、第二梯度值及 jet 重建全部式子。它验证原 Cramer 恒等式、所有 Strip 与商环精确除法、完整结式与 gcd、四个末纤维的 Gröbner 基和原分母平方归零身份。执行依赖 Python 3.12.14、SymPy 1.14.0、python-flint 0.9.0，所有计算均在特征零 $\mathbb Q$；计算数组只留在内存。

实际执行为 `PYTHONPATH=/tmp/isp-347c05929dd3/deps python 2026-11-26-unit211-opposite-regular-exceptional-curves-347c.py`，exit 0，程序计时 92.272577 秒，峰值 RSS 152380 KiB；源码 SHA256 为 `d7f3a0603557f177408150060c8fdec24b35a0bd4a3fa9a50ef2ed999f48177e`。首次全部数学核验通过后，仅最终 JSON 输出因 FLINT 整数序列化报错；只增加整数序列化支持后按上述字节完整复核通过。源码没有重跑已登记的 $\ell=0,1/2$ 或奇异 mean 面，只引用这些完整结论作为本图边界。

本条唯一使用物理几何排除的是第 2.2 节明确恢复的秩二 Gram；其他各支直接与原必要方程或已知非零分母矛盾。没有改变物理配对、丢掉原 jets、从必要范数条件反推充分性，或把几何排除当作全局幂恒等式。一般图 (5.4) 中剩余的有限候选仍须继续用完整原方程消除。
