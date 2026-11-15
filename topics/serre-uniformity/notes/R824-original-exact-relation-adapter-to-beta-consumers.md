# R824 的原五次准确关系：接入 R792 点值与后续正规坐标

日期：2026-11-15。状态：**以下来源转换与数学等价性已证明；实际接入必须另绑定 R824 已完成的准确关系 stage。本稿不把其模核、尚未完成的 Dixon lift 或尚未结束的 runner 当作准确关系。**

本接口保留原映射 $f_4:X_1\to C_b$、原模型 $C_b:y^2=x^3+b$、
次数 $1206$、$f_4(c_0)=O$ 和原点 $c_1=4424$。
它改变的是所消费的准确函数表达式来源。原 R787 保留列 $1186$ 的
计算继续；本接口不会重算、冒充或覆盖那个生产者。

## 1. 接受的实际来源

令 $H$ 为原 $Y$ 上次数 $272$ 的线丛，原 R786 已认证的五次基为
$F_0,\ldots,F_{1233}$。R824 的一个新完成 stage 给出

$$
A=\sum_i a_iF_i,\qquad B=\sum_i b_iF_i,\qquad
a_i,b_i\in L,\quad B\ne0.
\tag{A1}
$$

实际文件须是原冻结 R824 core
`1ece3cf45f57fda2d1fe40f38efb3e225d2e05ce910a917eb38dbcd85fe3d1cb`
写出的 `R824-power5-free-cccc-exact-generator.json.gz`。
其 `ordinary_power=5`、`original_basis_dimension=1234`、
`basis_integer_scale=82^10`、`candidate_only=false`、
`exact_original_A_equals_yB=true`、`B_nonzero=true`。
`cccc` 是实际已完成的新 free column，不能填原保留列 $1186$。

以下链全部保留原字节、原 configuration 和原 SHA：

1. 原 artifact/run/source/core、full manifest、run/core/public-input 回执；
2. 该准确 generator、原 target configuration 与原字段定义；
3. 原 R786 producer 身份和 `original_basis_index`；
4. 其全部 `full_relation_verification_stages`，各阶段按顺序覆盖
   $0,\ldots,128$，每阶的 $280$ 个原 $\mathbf Q$ 坐标已全部为零；
5. 同一候选、共同算子和最后 lift 的原引用。

已按 R824 规则删除的大验证乘积和旧 lift 只保其原 digest。
消费器不会把 digest-only 引用误当成仍存在的文件，也不会据此重算它们。
原共同算子的数组不需要再次下载；它的真实 file/bytes/SHA 和
各验证块的同一乘积 SHA 足以钉住已执行的原证明链。

允许两种已经结束的来源。第一种是有成功证书的 R824 run，其真实
generator index 包含该准确 stage。第二种是明确 source-bound 的预算
checkpoint：原 run/core 回执均为未完成，配置明确列出实际非零退出码，
但此 generator 及其全部验证块已经完成。第二种仅证明这个单独关系，
不声称整个 R824 scope 或全部 $272$ 个生成元已经完成。运行中的输出、
未绑定的工作目录、`candidate_only=true` 和任意未验完的 lift 都不接受。

## 2. 比值仍是原 y

R824 用原 R781 的 $\kappa,R_n$ 建立同一原 Laurent 算子。设 $v$ 是
所固定原尖点的参数。清分母后的 $129$ 条原关系是

$$
D_{129}\left(
246^3\kappa^{129}vA+
\sum_{n=0}^{128}R_n\kappa^{128-n}v^nB
\right)\equiv0\pmod{v^{129}},
\tag{A2}
$$

其中 $D_{129}\in\mathbf Z_{>0}$、$\kappa\ne0$。
由原 $y$ 的 Laurent 定义，(A2) 正是
$246^3D_{129}\kappa^{129}v(A-yB)$ 的完整截断，故 $v(A-yB)$
在该尖点至少消失到 $129$ 阶。

把 $A-yB$ 看作 $H^5(E_y)$ 的截面。原 $y$ 在每个尖点恰有一个
简单极点，因此上式的局部零阶计数正是此线丛截面的零阶，而不是把
$A-yB$ 的普通函数零阶少算一项。全部二十个原尖点在 $L$ 上形成一个
算术轨道；原关系及其 $L$ 系数经过同一 Galois 运输，在全部二十个
尖点具有同样的零阶下界。又

$$
\deg H^5(E_y)=5\cdot272+1206=2566<20\cdot129=2580.
\tag{A3}
$$

因此该截面恒为零，即 $A=yB$。由于 $B\ne0$，(A1) 的比值就是原
$f_4$ 的 $y$ 函数。这个论证不要求把 R824 的所有生成元都算完，也不
要求再次完成原 R787 的保留列。它直接消费一个已完成的原关系。

两个不同 free column 得到的 $(A,B)$ 一般不只差一个常数；它们可能
相差一个非恒定有理函数倍数。本接口只使用已经证明的比值相等。
不会把新 $(A,B)$ 的截面值、共同零或正规向量说成旧保留列的值。

## 3. 原字段与已经清去的共同标量

原输出采用

$$
B_{\rm fld}=\lambda b,\qquad s=1+2\zeta,\qquad
L=\mathbf Q(b,\zeta),\quad \zeta^2+\zeta+1=0.
\tag{A4}
$$

每条十四维行按 $j=0,1$ 在外、$i=0,\ldots,6$ 在内排列
$B_{\rm fld}^is^j$。R824 与 R792 的显示字符串不同，原字段定义、
$\lambda$、原 $b$ 最小多项式及原 R735 模型必须逐项一致；不改 twist，
也不替换原指定实嵌入。

若一条整数行是 $(u_0,\ldots,u_6,v_0,\ldots,v_6)$，则 R792 使用的
$1,\zeta$ 表示为

$$
\sum_{i=0}^6 (u_i+v_i)\lambda^i b^i+
\zeta\sum_{i=0}^6 2v_i\lambda^i b^i.
\tag{A5}
$$

后续 R809 若使用原 $b^i,sb^i$ 顺序，则仅对两块的第 $i$ 项各乘
$\lambda^i$。两种转换都只执行一次，不另乘 $\zeta$ 或实下降三同源。

R824 先对准确有理坐标清一个共同正分母 $d$，再从两个完整整数矩阵
同时除去共同整数 content $g$。最终保存的 $A,B$ 已同时乘以
$d/g$；`common_rational_denominator_cleared` 和
`common_integer_content_removed` 是原审计数据，不能再插回。
比值、原曲线映射和饱和极理想均不受这个共同非零常数影响。
这里的 $d$ 与 (A2) 的 $D_{129}$ 角色不同，不可混用。

## 4. R792 的最小来源变体

新读取模块 `scripts/R824_original_exact_relation_adapter.py` 只验证来源、
原坐标布局和完成证书，并返回原准确 $(A,B)$ 与显式来源 receipt。
它不生成假 R787 certificate，不重命名或改写任何原 producer stage，
也不做新域运算。

`scripts/R792_original_beta_from_R824_relation.py` 使用独立 result/tag，
来源集合是 R735、R775、R786、R790、R791、R824。
它精确绑定已冻结的
`R792_original_beta_composition.py`
（SHA256
`7b7a5483e560f2d244092af486c8aed606b18c1f3557dddb3b850a290b4e343d`），
复用其原截面合成、共轭唯一选根、原切向核验和三同源点公式。
新变体不会把自己的 source SHA 写成冻结框架的 SHA；二者在 tag 中分列。

首次只消费 R790 已认证的 $146$ 个原 M2 值及首 coarse jet，
按同一原 R775 power2--5 recipes 合成 (A1) 的四个值
$A_0,A_1,B_0,B_1$。原 $82^2$ 与 $82^{10}$ 尺度原样保留，
不重做旧 q 前缀、CM 迹、周期或 Hom 格。

若 $B_0\ne0$，得到 $y_0=A_0/B_0$。若两零阶均零而 $B_1\ne0$，
得到 $y_0=A_1/B_1$。分母相应为零而分子非零时给原点 $O$，同时
保留 R791 原非分歧对三阶极点的检查。
前两阶都共同为零时，只输出实际共同零阶至少二，并继续原局部评价；
不能标记点坐标已经完成。R790 的共同零上界 $154$ 对这个新五次表达式
同样适用，因为剩余有效基点除子的次数仍是 $5\cdot272-1206=154$。

有限分支沿用 R791 的真实共轭关系
$c(x_0)=\zeta^2x_0$、$c(y_0)=-y_0$，因此
$u_0=\zeta x_0\in\mathbf Q(b)$，且 $u_0^3=y_0^2-b$。
R792 的唯一原域立方根算法和实际三次同源都保持不变。输出仍首先是
$\beta_C=f_4(c_1)\in C_b(L)$，再是 $v\beta$ 的实际模型点；
不宣称选择了原抽象 $A$ 的某个同源核原像，不抹去 $\kappa v^\dagger v$。

## 5. 后续正规坐标接口

同一读取模块可把真实新 $(A,B)$ 交给 R809 的正规坐标消费者。
这需要把十四列按 (A5) 后所述的原 $b,s$ 顺序转换，再消费已完成的
原 S5 基、原短 minor 和模逆；不是重新生成 $1234$ 条旧 Q 行。

新的 target identity 必须含这个真实 R824 relation spec。
已经完成的 C0--C5、共同 S5 基和其原 tag 保持为独立来源；
不能因为新 consumer 的 source SHA 不同而重算它们，也不能把新
A/B target 误标成原 R787 保留列的 target。此处先给读取接口，
没有预称新的两组正规向量已经求出。

## 6. 文件与执行边界

新配置中 `relation_spec` 必须是真实已完成文件的
`file/bytes/sha256`，其 R824 run/source/artifact/manifest 均实际存在。
在该输出尚未发布前，工程只保 draft/pending，不触发算术。

所有新增字段转换、截面合成、立方根分解和点坐标核验仍只在公开仓库
Actions 运行。原数据和新证书只留当前一日 artifact；
Git 只保存脚本、参数、源身份与实际完成后的小 metadata。

依据：
[R824 原全局生成与关系判据](../results/R824-original-pole-module-generators-in-weights-five-to-seven.md)；
[R824 原准确关系算法](R824-original-global-polar-generator-consumer-method.md)；
[R792 原点值与共轭选根](../results/R792-original-beta-composition-and-Galois-cube-root.md)；
[R809 原正规坐标](../results/R809-original-normal-vectors-for-function-and-Hodge-inputs.md)。
