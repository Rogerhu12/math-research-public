# R1032：原最低型 CM 首 normal jet 的完整线性泛函

日期：2026-11-26。会话：Astra-serre-24b8836b-20261126；
global_route / root；normal gluing 与中心变形另经 o2_high_coefficient 纸审。

**已证明：在 R1029 的同一个整最低惯性型中，原 CM Abel 微分
的第 \(4m\) 个 normal 层由一个明确的底 Hodge 线性泛函给出。**
R1030 的实际整投影消去全部同阶低极部，保留下式的真实系数；
它不是将一个参考微分的系数规范为一。

该结论是原整格上的 graded jet 计算。它未宣称泛纤维第一个
Taylor 次数就是 \(4g-1\)，未控制更高 \(\pi_0\) 层中的低
\(t\) 次项，也未将整个类型块的线性代数替代某个实际半秩简单商的
Mordell–Weil 饱和格。

## 1. 原对象、底向量与结论

保持 R1018/R1023 的原曲线 \(X_1\)、原 CM 点 \(c_1\)、同一个
trace-zero ordinary quotient、原 Igusa 参数 \(b\) 及所有节点单位。
写
\[
p=12g-1>37,\quad m=(p-1)/2=6g-1,\quad
e_0=m(p+1),\quad \pi_0^{e_0}=p,\quad\varepsilon=\pi_0^m .
\]
令 \(S=\{A_p(s)=0\}\) 为 R1023 全部 \(e_s=1\) 尾的集合。
这些点不在 \(b^3=1\)。在 \(D_s\) 上使用原规范
\[
\omega_s=dX_s/Y_s,\qquad f_s=[z_s^{-m}],\qquad
\langle f_s,\omega_s\rangle=-2 .
\tag{1032.1}
\]
底特殊 Hodge 向量写成
\[
L=\sum_{s\in S}L_s\omega_s .
\]
原全局 Hodge 的自由性、base change 和 tame character 平均，
给权 \(m\) 的整提升 \(\Omega_L\)；最终使用 R1029 的
\(e_1\Omega_L\)。该类型块内的这种提升模 \(p\) 唯一。

定义
\[
R_L(b)=\frac2m\sum_{s\in S}\frac{L_s\theta_s}{(b-s)^2},
\qquad
\boxed{\quad \mathcal J(L)=\sum_{s\in S}
                         \frac{L_s\theta_s}{(1-s)^2}.\quad}
\tag{1032.2}
\]
\(\theta_s\) 完全沿用 R1023 的真实节点尺度。

原 \(c_1\) 尾为
\[
D:\ y^2=x(x^{2g}+A_{\rm tail}),\qquad
Q=(0,0),\quad t=\sqrt x,\qquad
F=x^{2g-1}y .
\tag{1032.3}
\]
保留下文实际 coarse/fine 比较的单位 \(\kappa_1\)。
本篇结论是
\[
\boxed{\quad
(e_1\Omega_L)|_D\equiv0\pmod{\pi_0^{4m}},\qquad
\overline{\varepsilon^{-4}(e_1\Omega_L)|_D}
       =\kappa_1R_L(1)\,dF .
\quad}
\tag{1032.4}
\]
除以 \(\varepsilon^4\) 后仅沿该分量读取首 normal 层，
不是声称这个除法给整个模型上的整微分。

## 2. 中心第 \(m\) 层的完整系数

在同一个 \(e_s=1\) 节点，R1018/R1023 给
\[
b_{\rm lift}-s=\varepsilon\theta_s z_s^{-m}
                                  +\text{更高层},
\qquad
\omega_s=-2z_s^{m-1}\,dz_s+\text{更高 }z_s\text{ 次项}.
\tag{1032.5}
\]
把中心微分 \(\varepsilon a(b-s)^{-2}db\) 拉回这个节点，
其尾首项是
\[
-\frac{am}{\theta_s}z_s^{m-1}\,dz_s .
\]
与 \(L_s\omega_s\) 比较，准确得 \(a=2L_s\theta_s/m\)。

中心第 \(m\) 层的惯性角色为零，所以下降为
\(\mathbf P^1_b\) 上的微分。
其极点只在 \(S\)，主部是上述 double poles；
每个 residue 为零，在三个 CM 标记及无穷远正则。
两种可能表达的差是 \(\mathbf P^1\) 上全纯微分，故为零。
因此完整中心层正是
\[
\boxed{\quad \varepsilon R_L(b)\,db .\quad}
\tag{1032.6}
\]
在无穷远，(1032.2) 为 \(O(b^{-2})db\)，也直接符合正则性。
没有丢掉一个额外的中心 holomorphic 自由项。

## 3. 逐 normal 层 gluing：中心自身变形也须保留

先说明下面的递推适用于实际模型。
在原节点
\[
zw=\rho\pi_0^e,\qquad \rho\in R^\times
\tag{1032.7}
\]
处，邻分量第 \(n\) 层的 regular Taylor 项
\(c\,w^k\,dw\)、\(k\ge0\)，给本分量的 polar 项
\[
-c\,\bar\rho^{\,k+1}
  \pi_0^{\,n+e(k+1)}z^{-k-2}\,dz .
\tag{1032.8}
\]
所以每阶新 polar part 只来自严格更低层的邻分量 regular part。
单位和坐标的更高项只能提高所需 normal 次数，或降低已经指定的
首极阶；原 \(\rho\) 没有被设成一。
每层在指定 polar part 后的自由项为该分量的全纯微分。

这里并不把中心 Igusa 曲线的全部形式变形视作常数。
可以在其带标记的正规化形式变形上，取一个足够大的有效极点除子
\(D_S\)，只支撑 \(S\) 中的标记。
因为
\[
H^1(I,\Omega_I^1(D_S))
 \simeq H^0(I,O_I(-D_S))^\vee=0,
\tag{1032.9}
\]
已知 meromorphic 项能逐阶提升，并始终在三个 CM 标记处正则；
再作 tame 平均保持原角色。
中心自身 smooth deformation 的非齐次项因此仍是这些标记处的
regular 输入，不会在没有节点输入的地方凭空制造新极点。
全纯的自由项仍须保留，不能由 (1032.9) 删除。

另一个独立条件是 principal parts 的可解性：
(1032.8) 的 polar 项没有 residue。
实际 compact-type 树的桥节点也没有非零 residue 流；
逐分量的 residue 定理从树的叶端起迫全部节点 residue 为零。
所以这里使用的 Mittag–Leffler 递推保留了真正的零 residue 条件。
(1032.9) 只处理正则化分量自身的逐阶提升，不被冒作这个
principal-parts 条件的替代。

CM 尾的仿射范围可使用 R1021 在整个 \(R/(p)\) 上的原模型；
节点处则始终按 (1032.7)–(1032.9) 递推。
这两个范围没有混同。

## 4. 所有低于 \(4m\) 的 CM 层为何为零

原 \(\Omega_L\) 权为 \(m\)，其特殊纤维只在 \(e_s=1\) 尾有分量。
中心的所有惯性角色为 \(p+1\) 的倍数，故在
\(0<n\le4m\) 中，中心只可能出现
\[
n=m,\qquad n=m+(p+1)=3m+2 .
\tag{1032.10}
\]
其它正整数层由完整惯性排除。

CM 尾的全纯微分角色为
\(3m(2j+1)\)、\(0\le j<g\)。
若它在权 \(m\) 的提升中作为第 \(n\) 层自由项出现，
必须 \(n+3m(2j+1)\equiv m\bmod e_0\)。
此范围的最小正 \(n\) 至少为 \((6g+4)m>4m\)。
因此直到第 \(4m\) 层都没有可加入的 CM holomorphic 自由项。

在中心第 \(m\) 层，(1032.6) 在 CM 标记正则。
因 \(b-1\) 在中心局部参数有阶 \(m\)，其 regular differential
的阶至少为 \(m-1\)。
实际 CM 节点厚度是三，故 (1032.8) 最早传入
\[
m+3((m-1)+1)=4m .
\tag{1032.11}
\]

现在假设按层归纳已有所有更早 CM 层为零。
中心第 \(3m+2\) 层在该 CM 节点的 polar part
只能来自更早 CM 层，故为零；
§3 保证中心自身变形不会另外制造该极点。
其角色为
\[
m-(3m+2)=-(p+1)\pmod{e_0},
\]
即 R1028 的 \(u^{-2}\) 微分角色。
只要在 CM 节点正则，这个角色迫其阶至少为 \(2g-2\)。
所以它最早传入
\[
(3m+2)+3((2g-2)+1)=4m .
\tag{1032.12}
\]
若有最早的非零 CM 层 \(n<4m\)，它既不可能有 incoming
polar part，也没有该角色的全纯自由项，矛盾。
这完成归纳，并排除了所有更早的 CM 返回。

第 \(4m\) 层时，中心 \(m\) 层贡献极阶至多 \(6g=m+1\)，
中心 \(3m+2\) 层贡献极阶至多 \(2g\)。
其它 supersingular 尾的反复反馈可改变第二个中心层，
但不能改变已确定的第一个中心层，或产生更高的 CM 极部。

## 5. 同一个原 quotient 给最高极部的系数

必须使用 R1018 §7 的同一个 trace-zero \(Q=sP\)，
不能替换成另一条 ordinary quotient。
R1021 的实际 target fine 参数满足
\[
u'=\varepsilon(c_Q\psi+pR_Q)
\]
于原仿射范围，\(c_Q\) 为原单位；
原 coarse \(b-1\) 在这个 fine CM 参数处恰有三次零。
因此保留一个准确的原单位 \(\kappa_1\)，有
\[
b_{\rm lift}-1
 =\kappa_1\varepsilon^3\psi_3+\text{更高层},
\qquad \psi_3=\beta^{3(p-1)}.
\tag{1032.13}
\]
R1018 (1018.23) 在同一个 ordinary 无穷支给
\[
\psi_3
 =z^{-m}(1+A_{\rm tail}z^{4g})^{-3/2}
       +\text{足够高的 }z\text{ 次项}.
\tag{1032.14}
\]
所需截断次数小于 \(p\)；这里没有在特征 \(p\) 中任意定义无限分数幂。

(1032.6) 因而在第 \(4m\) 层给最高 polar part
\[
\kappa_1R_L(1)\,d\psi_3,\qquad
[z^{-6g}dz]= -m\kappa_1R_L(1).
\tag{1032.15}
\]
\(\kappa_1\) 包含原节点、coarse/fine 及 target generator 的尺度，
没有被置成一。
第 \(3m+2\) 中心层的极阶至多 \(2g\)，故不改变这个系数。

作为与原局部源的额外核准，(1032.14) 的完整负主部为
\(z^{-m}-(3A_{\rm tail}/2)z^{-(2g-1)}\)。
而 \(F=x^{2g-1}y\) 的负主部为
\(z^{-m}+(A_{\rm tail}/2)z^{-(2g-1)}\)，且
\(x^{2g-1}dx/y\) 的主部为 \(-2z^{-2g}dz\)。
所以这一参考 \(d\psi_3\) 的第二类延拓为
\[
dF-A_{\rm tail}(2g-1)x^{2g-1}dx/y.
\]
最终证明只使用 (1032.15) 的最高系数；
不把这个参考式误作已包含全部中心反馈的原微分。

## 6. 完整角色空间和实际整投影

第 \(4m\) 层在 \(D\) 上的角色为 \(-3m\)，
极只可能在无穷远，极阶至多 \(6g\)。
记
\[
\mu=x^{4g-1}dx/y,\qquad \nu=x^{2g-1}dx/y.
\]
全部 affine 正则微分可按 \(x^jdx/y\) 和 \(x^jdx\) 分解。
第二类的角色是偶数倍 \(3m\)，不能等于 \(-3m\)。
第一类的角色条件和极阶界分别为
\[
j\equiv2g-1\bmod2g,\qquad 0\le j\le4g-1 .
\]
所以完整所需空间恰为
\[
\langle\mu,\nu\rangle=\langle dF,\nu\rangle .
\tag{1032.16}
\]
没有遗漏一个同角色的 holomorphic ambiguity。

由 (1032.15) 及 \(dF\) 的最高系数 \(-m\)，原首层必为
\[
\kappa_1R_L(1)dF+b_L A_{\rm tail}\nu .
\tag{1032.17}
\]
这里 \(b_L\) 保留全部第 \(3m+2\) 中心层、非齐次变形和 R1028
任意提升修正，没有被假定为零。
此式在全部配对分支上运输：
\(dF\) 已 \(N\)-不变，另一个不变微分是 \(A_{\rm tail}\nu\)；
按 R1030 的 norm 轨道比较，其两个系数在同一来源的分支并上为常数。

R1030 的真实整投影逐 normal 层相容，且
\[
E=e_1,\qquad E(dF)=dF,\qquad E(A_{\rm tail}\nu)=0.
\]
应用于 (1032.17) 得 (1032.4)。
这一步在所有配对分支同时完成，不能先把单一分支的
\(A_{\rm tail}\) 从 \(E\) 中提出。

## 7. 原 marked jet 与首 log 的同格坐标

在原 \(Q=(0,0)\)，
\[
F=t^{4g-1}\sqrt{A_{\rm tail}+t^{4g}} .
\]
故 (1032.4) 的准确首 \(t\)-项为
\[
\boxed{\quad
\overline{\varepsilon^{-4}(e_1\Omega_L)|_D}
 =\kappa_1\frac2m\,\mathcal J(L)
   \left((4g-1)\sqrt{A_{\rm tail}}\,
          t^{4g-2}+O(t^{8g-2})\right)dt .
\quad}
\tag{1032.18}
\]
共乘系数为单位，因为
\(4g-1=(p-2)/3\ne0\bmod p\)。
\(\mathcal J(L)\) 本身可能为零；结论给整个实际线性泛函，
不声称每一个底向量都有单位 jet。

若只积分读取次数 \(4g-1<p\) 的系数，积分分母为单位。
以 (1032.1) 的同一个配对记号写出原 Abel-log 系数向量，
得到
\[
\boxed{\quad
-\frac{\kappa_1\sqrt{A_{\rm tail}}}{m}\,
 \varepsilon^4
 \sum_{s\in S}\frac{\theta_s}{(1-s)^2}f_s .
\quad}
\tag{1032.19}
\]
这与 R1023/R1029 的原首对数列
\[
\varepsilon\sum_{s\in S}
       \theta_s(\lambda(s)+R_p(s))f_s
\tag{1032.20}
\]
在同一个整类型块、同一 \(\theta_s\) 坐标和同一底配对中表达。
两个列的不同全局单位与各自 \(\varepsilon\) 次数均保留。

必须准确区分后继问题：(1032.19) 是第 \(4m\) normal 层内
指定 Taylor 次数的系数；更高 normal 层可有更低 Taylor 次数。
它没有给整个原 Coleman/Abel 级数的统一尾项估计。
此外，实际半秩商的有理 \(F_0\)-作用可能带 \(p\) 分母，
所以排除 (1032.19) 为 (1032.20) 的一个普通标量倍数，
不等于排除它属于真正的饱和 \(F_0\log\beta\) 空间。
所选 \(\mathbf Q\)-简单商的 Néron 相对格、该 MW 空间、
原盘半径和 O0 覆盖仍须继续完成。

## 来源与审核

- [R1018](R1018-original-CM-divisor-exact-first-formal-layer.md)，
  原完整角色、同一 trace-zero quotient、§7 (1018.23) 的实际三次商展开。
- [R1021](R1021-actual-full-p-affine-tail-rigidity-and-quotient-parameter.md)，
  实际仿射模型、所有 level 作用及 target fine 参数；不挪用到整个中心或节点。
- [R1023](R1023-original-CM-divisor-complete-first-log-vector.md)，
  原 \(S,\theta_s,f_s\)、节点规范、全部首 log 和配对。
- [R1028](R1028-original-Igusa-Kummer-model-and-same-order-CM-jet-correction.md)，
  原 Igusa Kummer、CM 处 \(u^{-2}\) 的最小正则阶、厚度三及完整提升差。
- [R1029](R1029-original-lowest-inertia-type-integral-Hecke-splitting.md)，
  真整类型块及同角色提升模 \(p\) 唯一。
- [R1030](R1030-integral-finite-corner-projector-and-original-CM-affine-action.md)，
  真有限角、全分支运输及两个准确投影恒等式。

global_route 与 root 逐项核 normal 层、中心 smooth deformation、
原节点单位、所有 residue、两个唯一中心层、完整极部角色空间、
真实最高系数及原 Serre 配对；o2 独立核中心提升和 gluing 归纳。
没有数学程序或有限窗口重算。
Serre 主目标仍 OPEN。


## R1033 接续：原有理盘共同尺度

[R1033](R1033-original-rational-CM-disc-exact-lowest-type-scale-and-tail.md)
已将本篇的完整 normal 下界和最高系数换回
\(w=(a-1)/p^3\)。原 type1 Abel-log 与 formal map 除 \(p\varepsilon\)
后为整 Tate 级数，模 \(p\) 次数至多 \(4g-1\)，整个类型块最高系数非零，
故共同 \(M=1\)。全部 \(p\) 倍积分分母已纳入。
最低非零 \(w\) 项、真实 MW 饱和消去和具体 Néron 商格仍不由此自动确定。
