# 原 S2 的头来源与三叶共同 Schur：新必要充分输入

日期：2026-11-28（Asia/Taipei）  
会话：Astra-ISP-8542378f-20261127

状态：以下原来源分解、秩一行列式身份和严格正因子消去已证明；
头来源及三个条件 Schur 系数的全域正性尚待本次唯一首次返回。

唯一源为
[原头来源与三叶共同 Schur](2026-11-28-one-pair-four-independent-s2-head-leaf-rank-one-source-8542.py)，
Git blob 9f120fe91aa743c8e7f99d943e605611eeba0a11。
固定 180 秒、4 GiB，只打印普通小摘要，不保存或传出展开数据。
[原四维谱门](2026-11-28-one-pair-four-independent-s2-trace-first-boundary-receipt-8542.json)
已经冻结：本源不计算它未返回的 $c_2$，也不重测已付总迹。

## 1. 原共同四维形式没有更换

六位正权仍为
$$
(\sqrt{x_1},\sqrt{x_2},\sqrt{x_3},\sqrt{x_4},1,1),
\qquad x_1\ge x_2\ge x_3\ge x_4>0.
$$
头为 $X_1$，pair 为 $J$。
本次使用[原完整来源](2026-11-28-one-pair-four-independent-s2-four-source-companion-spectrum-8542.md)的同一个
$$
Z=U_1-\widehat K-\Lambda_1\Lambda_2^{-1}\Lambda_1.
\tag{1}
$$
这里 $\widehat K$ 保整个六维上来源、完整上精度逆及两个 mixed term，
全部 $\Lambda_j$ 先在整个五维低物理层取逆再压到四源。
$U_1$ 是这四个原 primitive 源的物理 Gram。
没有重新定义一个较短的低来源或把普通转置当作物理伴随。

完整 S2 就是原 $Z>0$。
上一次只证明 $\operatorname{tr}(U_1^{-1}Z)>0$，不支付本稿任一新标量。

## 2. 第一个新目标是一个指定的物理来源

将四个源准确分成
$$
v_0=X_1-J,\qquad v_i=X_i-J,\quad i=2,3,4.
$$
它们不是正交基，但都是原真实来源。
原二次型据此写为
$$
Z=\begin{pmatrix}h&z\\z^{\mathsf t}&Z_{\rm leaf}\end{pmatrix}.
\tag{2}
$$
新首目标是
$$
\boxed{h>0.}
\tag{3}
$$
它严格支付同一个头减 pair 来源 $v_0$ 上的全部 S2 费用，
与原总迹或原第二特征系数不同。
源码先完成 (3) 的五个闭权序证书；若有一个未付即停止，
不使用未经证明正的头枢轴。

在 $h>0$ 后，完整原 (1) 严格正当且仅当
$$
\boxed{S_{\rm leaf}=Z_{\rm leaf}-z^{\mathsf t}h^{-1}z>0.}
\tag{4}
$$
这是对每个相同叶坐标 $\xi$ 真实最小化
$(\xi_0,\xi)^*Z(\xi_0,\xi)$，
头坐标准确取 $\xi_0=-h^{-1}z\xi$。
因此 (4) 保所有头叶 cross，没有把某个叶压缩的正性冒充完整 S2。

## 3. 同一原叶度量与三项秩一身份

令 $G$ 是三个原来源 $X_i-J$（$i=2,3,4$）的完整物理 Gram，
也就是 $U_1$ 的叶主块，故 $G>0$。
新三个系数始终定义为原连续比值
$$
\frac{\det(tG+S_{\rm leaf})}{\det G}
=t^3+\frac{n_1}{h}t^2+\frac{n_2}{h}t+\frac{n_3}{h}.
\tag{5}
$$
为直接保秩一来源而不对整个条件矩阵再作非交换特征递推，置
$$
R=G^{-1}Z_{\rm leaf},\qquad v=G^{-1}z^{\mathsf t},\qquad
\mu_j=zR^jv\quad(j=0,1,2),
$$
$$
e_1=\operatorname{tr}R,\quad
e_2=\sum_{i<j}(R_{ii}R_{jj}-R_{ij}R_{ji}),\quad
e_3=\det R.
$$
那么准确有
$$
\boxed{
n_1=he_1-\mu_0,\quad
n_2=he_2-e_1\mu_0+\mu_1,\quad
n_3=he_3-e_2\mu_0+e_1\mu_1-\mu_2.
}
\tag{6}
$$
证明只需三阶原伴随矩阵恒等式
$$
\operatorname{adj}(tI+R)
=t^2I+t(e_1I-R)+(e_2I-e_1R+R^2)
$$
以及
$$
\det(tI+R-vz/h)
=\det(tI+R)-h^{-1}z\operatorname{adj}(tI+R)v.
$$
这两式在整个多项式环成立，不先要求 $tI+R$ 可逆。
由此直接得到 (5)–(6)。
特别地，三项 $n_j$ 中只出现一次 $h$；未先造出 $h^{-2},h^{-3}$ 再靠不明约分消去。

因为 $h>0$，三个新符号目标就是 $n_1,n_2,n_3>0$。
原 $G^{-1}S_{\rm leaf}$ 相似于真实 Hermitian 矩阵，
所以三个系数全严格正当且仅当三个原广义特征值全正：
正系数排除 $t\ge0$ 上的根，反向由正特征值的初等和成立。
结合 (3)，这是完整 $Z>0$ 的必要充分分解。

## 4. 三叶坐标、碰撞和严格正因子

互异叶权上仍用 $a=x_1$ 与叶初等和 $(s,p,q)$。
令 $V_{ik}=z_i^k$。
头坐标不变，原叶源作 $V$ 变换，于是
$$
h\mapsto h,\quad z\mapsto zV,\quad
Z_{\rm leaf}\mapsto V^{\mathsf t}Z_{\rm leaf}V,\quad
G\mapsto V^{\mathsf t}GV.
$$
原 (5) 的分子分母中 Vandermonde 平方完整相消。
$e_j$、$\mu_j$、$n_j$ 都是同一原连续不变量。
重复权处不称退化 Hankel 是真基底；
原 $U_0,U_1,\widehat C_1,\Lambda_2,\Lambda_3,G$ 和完整物理 Gram 全正，
对三个叶置换的原正分母取乘积即可支付约简后全正域无极点。

在正确的五个闭权序中，代换仍为
$$
a=P_a/\tau,\quad s=P_s/\tau,\quad p=P_p/\tau^2,\quad q=P_q/\tau^3,
$$
故使用权 $(1,1,2,3)$ 齐次化，乘的 $\tau^d$ 严格正。
源码对每个新目标先允许消去以下严格正的原因素：
$$
a,\ s,\ p,\ q,\ a+1,\ e_1^{(6)},\ldots,e_5^{(6)}.
$$
这里后五项是原六个平方权 $(a,z_1,z_2,z_3,1,1)$ 的初等和：
$$
e_1^{(6)}=a+s+2,\qquad
e_2^{(6)}=p+as+2a+2s+1,
$$
$$
e_3^{(6)}=q+ap+2p+2as+a+s,
$$
$$
e_4^{(6)}=as+(2a+1)p+(a+2)q,\qquad
e_5^{(6)}=ap+(2a+1)q.
$$
它们在全部正权处严格正，包括所有碰撞。
只在完整因子确实整除分子时消去，且每次实际乘回原多项式。
没有除以可能在碰撞为零的判别式，也没有把一个未证正的 Schur 因子约去。
余下五域仍用完整系数证书或固定局部平方，正常数和完整返回均保留。

## 5. 全部成功之后的准确七位接口

只有头标量及三个条件谱系数在全部闭域严格正，
才得到原对称低四维 $Z>0$；
加旧出生一 singlet 费用至多 $2/3$，才给整个低五维 S2。
若只支付 $h$ 或某个 $n_j$，不作这一收尾。

为明确费用不遗漏，完整成功后，在同一个旧六位原上下来源上定义
$$
\kappa=\|F^{-1/2}\Delta L_3^{-1}\Delta^*F^{-1/2}\|<1,
$$
$$
\sigma=\|A_{\rm op}^*G_1A_{\rm op}+L_1L_2^{-1}L_1\|<1.
$$
新已付九维 S1 给 $\kappa$，本次全五维 S2 才给 $\sigma$。
已付六独立权内部第二边给 $\rho=1/2$；
[原六位统一首边](../results/R271-appendix-quantitative-one-bit-source-transfer-and-six-site-319-over-320.md)
给 $F\ge C_1^2/320$。
所以同文的完整定量返回，保同一个 $Qy$、$W_tW_t^*$ 和实际新 $H_0$，可取
$$
\alpha(b)=\min\{1-\sqrt{\sigma},\ (1-\sqrt{\kappa})(1-1/\sqrt2)\}>0.
$$
新增任意第七正权 $t^{1/2}$ 后，整个十四维原出生二首边才可得
$$
\Gamma_1^{(7)}(\Gamma_2^{(7)})^{-1}\Gamma_1^{(7)}
\preceq(1-\alpha(b)/640)I.
$$
对同一旧六权取倒数，再用已付全出生真实倒数权对偶，支付合法末边；
两边可共用
$$
c(b)=1-\frac{\min(\alpha(b),\alpha(b^{-1}))}{640}<1.
$$
该常数对新第七权一致，但依赖旧六权。
这里所有陈述都明确以本次完整 S2 成功为前提。
此有限 primitive 接口仍不等于原 $W$ 的 Green 来源费用或 $N=M$。
