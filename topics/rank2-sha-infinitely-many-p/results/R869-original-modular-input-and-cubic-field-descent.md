# R869 — 原小模方程的公开精确结果与首 Hom 的三次域下降

日期：2026-11-16。

**状态：下述代数下降已证明，固定模方程与三份微分前缀已在公开 Actions 用精确运算生成。** 尚未认证原函数坐标，未断言 $n=1$ 整，也未得到原非零 shadow。

## 1. 原首 Hom 在 $\mathbf Q(v)$ 上下降

保持 R862/R864/R866 的 $h,t=h^3,v=t/2^{32}$。
最初可以选择非零实17挠点 $P\in E_0[17](\mathbf R)$：实椭圆曲线的恒等分支含此点。
$\rho_{17}$ 不因把非零 $\mathcal O_K/17$ 基点乘一个单位而改变，所以这不更换原有限角色或 Artin 方向。

复共轭把 $[u]P$ 送到 $[\bar u]P$。唯一的阶32子群 $G_{32}$ 共轭稳定，故实际乘积
$$
h=\prod_{u\in G_{32}/\{\pm1\}}X([u]P)
$$
固定于复共轭。于是 $v$ 是 R864 的指定实嵌入坐标。记
$$
F=\mathbf Q(v)\simeq\mathbf Q(\sqrt[3]{17}),\quad
L=F(\omega),\quad \iota=\text{复共轭}.
\tag{1}
$$
$F$ 的签名为 $(1,1)$，不是原 newform 的全实三次 Hecke 系数域。
这里只使用指定实嵌入及 $L/F$ 的二阶下降。

对素于 $34\delta$ 的理想，原 ring-class Artin 元满足
$$
\sigma_{\bar{\mathfrak a}}=\sigma_{\mathfrak a}^{-1},
\qquad \iota\sigma_{\mathfrak a}\iota=\sigma_{\mathfrak a}^{-1}.
\tag{2}
$$
第一式来自 $\mathfrak a\bar{\mathfrak a}=(N\mathfrak a)$ 及有理主理想的平凡 ring-class 像；
第二式是同一理想共轭的 Artin 相容性。
原 $E_0/\mathbf Q$ 同时给
$\overline{\psi_0(\mathfrak a)}=\psi_0(\bar{\mathfrak a})$。

R862(40)–(41) 的好位项为
$$
[q^m]H_0=\frac1h\sum_{N\mathfrak a=m}
 \psi_0(\mathfrak a)h^{\sigma_{\mathfrak a}^{-1}}.
\tag{3}
$$
将其共轭，$\mathfrak a$ 项正好变成原 $\bar{\mathfrak a}$ 项。
包含 $(2)^r$ 的项另乘准确实数 $(-2)^r$，因此完整 primitive 级数也固定。
又 $H_0\in L[[q]]$，故
$$
\boxed{H_0\in F[[q]].}
\tag{4}
$$
这是全部系数的证明，不是从541个样本推断。

目标 $C_v:Y^2+vY=X^3$、$J_0(2601)$ 和基点 $\infty$ 都在 $F$ 上。
$\Xi_0$ 与其共轭在 $\omega_v$ 上的拉回由(4)相同。
特征零 Hom 微分表示单射，故 $\Xi_0^\iota=\Xi_0$；
对 $L/F$ 作真实 Galois 下降得到
$$
\boxed{\Xi_0\in\operatorname{Hom}_F^0(J_0(2601),C_v).}
\tag{5}
$$
清分母后的同一 $n\Xi_0$ 也在 $F$ 上，故首映射重建可用三维常数域。
其余两条由 R867 的真实整 $T_7$ 恢复，再以 $57n$ 清原 $b$-基。
回原 $E_0$ 的 $2^{11}\kappa$ 和全部 Artin 系数仍保留。
若起初采用另一个17挠点，应同步共轭坐标与原映射，不能只移动 $h$ 而固定外部系数。

## 2. 原 Hecke 方程的精确结果

R866(16)–(20) 的整数 eta、Faber 和 Newton 构造已在公开 producer 执行，得到同一个
$\Phi_{17}(T(z),T(17z))=0$，$T=(\eta(z)/\eta(9z))^3$。
完整输出给
$$
\boxed{\deg_X\Phi_{17}=\deg_Y\Phi_{17}=18,\quad
\deg_{\rm total}\Phi_{17}=34,\quad
\#\operatorname{supp}\Phi_{17}=291.}
\tag{6}
$$
最大整数系数绝对值为78 bits；同次完整运算核得
$$
\Phi_{17}(X,Y)=\Phi_{17}(Y,X),\quad
\Phi_{17}(X,0)=X^{18},\quad [X^{17}Y^{17}]\Phi_{17}=-1.
\tag{7}
$$
这不是拟合：R866 已证明该有限构造就是原18个 Hecke 根的乘积。
每次 Newton 除以 $m$ 均在完整整数系数列表核整除，Faber 最大为306。

初始输入同时给
$$
T=q^{-1}-3+5q^2-7q^5+3q^8+15q^{11}-32q^{14}
 +9q^{17}+O(q^{20}).
\tag{8}
$$
使用该方程的 $18\times17$ 非回溯 tower 时，仍取光滑正规化并保特殊点重数。

## 3. 三份原微分前缀

producer 在固定 $\mathbf F_{289}$ 中建立原 $\alpha=-1+2\omega$ 的288阶表，
按 R866(29) 枚举范数至541的理想，各 $\mu_6$ 轨道一次，且仅删 $17\delta$ 的倍数。
共有217个原好理想；全部运算在精确数域中完成。
由实际 $\ell$ 恢复 $\tau$，再按 R866(32) 得三条完整前缀。
每条在 $1\le m\le541$ 恰有98个非零系数，均位于 $m\equiv1\bmod3$。
首项和完整二处项为
$$
(h_{0,1},h_{1,1},h_{2,1})=(1,u_1,u_2),\qquad
(h_{0,4},h_{1,4},h_{2,4})=-2(1,u_1,u_2).
\tag{9}
$$
例如原第一条7系数准确为
$$
\boxed{h_{0,7}=
\frac{1378521263+57978976034v+157811v^2}{531360}.}
\tag{10}
$$
原本征形式的7系数在 $1,b,b^2$ 基中为 $(0,1,7/c)$，
与 R867 的 $t=b+7/b$ 相符。§1的一般证明解释其 $F$-值，
不能因此把 $H_0$ 当作一个新有理系数本征形式。

本次未给函数候选。必须先满足 R866 的完整椭圆函数恒等式和原基点条件，
才能由541项微分认证原 Hom；非零首项不替原 Chow 类或 shadow 非零。

## 4. Producer、运行与哈希

- 脚本：[produce-original-modular-function-input.py](../scripts/produce-original-modular-function-input.py)。
- 参数：[original-modular-input-request.json](../ci/original-modular-input-request.json)：固定17、Faber306、CM精度541。
- workflow：仓库根 $.github/workflows/rank2-sha-original-modular-input.yml$。
- 源码提交：$f748d7a860269df6548542ba016b4fe45ea80d9b$。
- 公开 [run 43825112263](https://github.com/Rogerhu12/math-research-public/actions/runs/43825112263)，job $133156983241$，attempt1；
  2026-11-16 07:38:15 UTC完成，数学部分约0.529秒，Sage10.6。
- image：$sagemath/sagemath@sha256:19995db6194f4a4bab18ce9a88556fd15b9ed5e916b4504fefe618a7796ddbdb$。
- 脚本 SHA-256：$5da00865767302681c6f20230b7cf227f9b29d57b8499de8956235ac9d0d3e14$。
- 完整输出 SHA-256：$2f949c372dddac503b83d9801b9d206bc030768b2c636c3563036423c7e403cb$。
- $\Phi_{17}$ 规范项表 SHA-256：$0bbf83ac9d6435a446f43e909333f7159b30fc52134e9de966298f56a7b859be$。
  编码为排序后的 $[X\text{-次数},Y\text{-次数},\text{整数字符串}]$。
- 三条 $H$ 完整规范前缀 SHA-256：$d9c63c72ee06325e23c204dd9adae1abf97bad141c2697d21f0338586b561e62$。
- 原本征形式 $b$-基前缀 SHA-256：$3627557a89d8b8296d87e5ba729f0d98bd338a230063052e0d216a9866f00bd1$。

只保脚本、参数、run/hash及数学结论，不保存291项方程、541项序列或其它重算输出。
后续以同一个原 $R$ 商低权模形式重建原映射；原循环非零与主目标仍未完成。
