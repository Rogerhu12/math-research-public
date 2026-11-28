# R147 LCW：直接消费原完整几何累计值的实际 cap 锚改进

**已证明。** 2026-11-28。对 [CW](R147-supplement-actual-cap-world-anchors-and-supported-nu-height.md)
的同一个实际 reflected M cap、同一个 axial world 和其下方
selected passive core，原 $b=9/50$ 锚可改进为

$$
 a_0<.001314673,\qquad p_0<.002603805,\qquad
 a_1<.008949,\qquad b_1<.028185.                 \tag{LCW.1}
$$

$p_0$ 仍是模同一个整体常数的位置差。于是原 H96 的两项
actual-anchor 费用分别可用
$ .018681\,H_j$ 与 $.003503042\,G_j$；完整公式见第5节。
它们保留同一相对参考数值误差，没有改动任一已成 RHI、WMR
或 height integral。原未匹配的 passive core 仍未被称作真 GC 解。

## 1. 整个原输入的恢复与准确区间

[C](R133-supplement-complete-C0-state-and-nu-geometry-response.md)
的原 native 已存每盒从 $R=25/8$ 向内的完整累计连接、位置
双积分和参考长度。此次按其
[原 identities](../notes/2026-11-14-R133-complete-C0-state-nu-geometry-response-identities.json)
从提交 `1352e025222a3dac0740a7ec3a9b64cdd30bdb0a` 恢复整个
`2026-11-14-R133-complete-C0-state-nu-geometry-response-native.json.gz`：
4,073,131 bytes，SHA256
`00efc0322a9aa82cd1f234899599ed3fbaff87edd35b8c9ac1331b229b276a55`。
已核完整 source SHA、candidate、固定准确 $\eta_0$、两个原
radius、全部7722行及连续覆盖 $[0,25/8]$。

这次没有计算任何旧盒增益或积分。以下原 whole records 的
`upper` 本身是完整 decimal ball；比较时还取它的 outward upper，
不读取其 diagnostic floating midpoint。

| 原 row / 字段 | 完整已存 ball | 新有理上界 |
|---|---|---:|
| 6376 / state_to_frame | `[13.237874173951901018169116388832004 +/- 4.56e-34]` | 13.237875 |
| 6376 / state_to_position | `[7.7220473944036279418396656084178863 +/- 1.27e-36]` | 7.722048 |
| 6376 / frame_anchor_to_position | `[0.58339766616434506024683891599567426 +/- 9.41e-37]` | .583398 |
| 1753 / state_to_position | `[26.219221594419499078402401149485263 +/- 4.71e-34]` | 26.219222 |
| 1753 / frame_anchor_to_position | `[1.7134937145270481072833155424895293 +/- 4.22e-35]` | 1.713494 |

row6376 的准确闭区间是

$$
 \left[\frac{4052614164685201}{4503599627370496},
       \frac{8106479329266893}{9007199254740992}\right],
 \qquad L=9/10\text{ 在其中}.                         \tag{LCW.2}
$$

原累计值对应左端，故由 integrands 非负直接上界 $[L,R]$。
没有按长度比缩小一个 norm。row1753 的准确左端就是 $b=9/50$，
其右端是 $3244468231551495/18014398509481984$。
两个 row 的 `nu_to_frame`、`nu_to_position` 均准确为零；
整个 $[b,R]$ 位于原 compact metric bump 的支撑外。

这里仅限制完整正积分，未用两个旧 upper 相减恢复未知系数。
例如不把两个 `frame_anchor_to_position` upper 相减后称作
$[b,L]$ 的新长度 upper。

## 2. 同一实际 cap 的新 $L$ 值锚

[CG](R133-supplement-actual-cap-in-final-geometry-C0-ball.md)
已对同一个真正存在的 M 固定点证明

$$
 \max(\|u_*-u^0\|_\infty,\|v_*-v^0\|_\infty)
 < e:=.000099309,\qquad L\le r\le R.                  \tag{LCW.3}
$$

该界包含全部 angular modes、真实 mean 和连续修补。
保留 CW 原 product/有限正则性域；本条不扩大 $\gamma$ 或 $f_B$
输入球，也不从未知 core 自动断言这些输入合格。
原 RA 的实际 $R$ 锚为 $r_q=10^{-12}$、$r_f=6\,10^{-21}$，
并保留同一个整体 $\lambda$。

使用 C 的准确正交 Duhamel 和同盒三角双积分公式，直接代入
上节已经保存的累计值：

$$
\begin{split}
 A_{0,L}&<r_q+13.237875e<.001314641,\\
 P_{0,L}&<r_f+.583398r_q+7.722048e<.000766936.
\end{split}\tag{LCW.4}
$$

同 CW 一样，这些公式适用于竖直 row 和竖直 position；没有
把一个未支付的全 world frame 初值误差代入。位置的常数仍是
RA 那一个 $-\lambda$，未在 $L$ 另作平移。

## 3. 真实 angular GW 与 selected core 的完整传播

CW.16–24 的实际 angular GW、原 raw angular defects 及原系数
保持不变。因此

$$
\begin{split}
 A_{1,L}&<2.157A_{0,L}+4.073e+3.127699\,10^{-8}<.003242,\\
 B_{1,L}&<4.001A_{0,L}+4.131e+4.956566\,10^{-8}<.005672.
\end{split}\tag{LCW.5}
$$

这里一阶导数来自 cap 的真 GW 方程，绝不是对 (LCW.3) 的
$C^0$ 界求导。原残差非零的 raw reference angular defects
仍分别完整加入。

应用 [ACT](R147-supplement-selected-core-C1-anchor-transfer-and-weak-height-ports.md)
的原已付同对象有限中心传播，得到

$$
\begin{split}
 a_0&\le A_{0,L}+3.148\,10^{-8}<.001314673,\\
 a_1&\le A_{1,L}+4.312A_{0,L}+3.6461\,10^{-5}<.008949,\\
 b_1&\le B_{1,L}+1.950541A_{1,L}
                     +12.205365A_{0,L}+1.41\,10^{-4}<.028185.
\end{split}\tag{LCW.6}
$$

在整个 $[b,R]$，同一连续 piecewise passive model 的 state
error 受 $e$ 控制：cap 用 (LCW.3)，core 用 ACT 的 $2\,10^{-9}$。
其 compact metric difference 在这段准确为零。故无需以粗的
全 $[0,R]$ position 系数30.196406付费；直接使用 row1753 有

$$
 p_0<r_f+1.713494r_q+26.219222e<.002603805.          \tag{LCW.7}
$$

这又保持原 R 高度常数。core/cap curvature match 仍是另一条
未解方程；被动 radial frame/position 本身按定义连续，因此
(LCW.7) 不引入一个隐含的几何 jump。

## 4. 同一 supported particular 的高度 pivot

代入原
[WRA](R147-supplement-actual-anchor-sensitive-weak-height-receiver.md)
完整四个弱接收器，得到

$$
 |\mathcal L_b(h)|<94360(D_*+J_-)+6676F_-
                         +3014F_{\rm st}+8884J_{\rm st}.
 \tag{LCW.8}
$$

全部原 root/strict source spaces、ordinary $dr$、两 mean 和
独立 varying world ports 均保持。对 CW 指定的 NP particular，
冻结整个 $r\ge b$ exterior、cap 输入和这一个 world placement，
仍由同一几何 ODE 唯一性给 $K_b=Y_b=0$。

[AWH](R147-supplement-actual-complete-reference-world-height-and-anchor-budget.md)
的原完整 kernel 与 density norm 不重算：其 actual-anchor 费用为

$$
 .031082487a_0+.006877446p_0<.00005878.
 \tag{LCW.9}
$$

结合原完整 reference height $[-.0253702,-.0252298]$，这同一
未归一化 actual cap-anchored particular 满足

$$
 \boxed{-.025429<c_H<-.025171<0,\qquad |c_H^{-1}|<39.73.}
 \tag{LCW.10}
$$

这可直接消费于后续 height-first Schur，但未把 particular
改称已经完成所有 boundary/finite/high 约束的解。

## 5. H96 的实际替换槽

对 [H96](R149-supplement-complete-height-row-on-original-finite-trials.md)
的同一整 trial 列，记原数值 kernel 误差 $k_q,k_f$ 和原完整
receiver norms $H_j,G_j$。它的完整锚费保持原公式

$$
 (k_q+a_0)14.20875H_j+(k_f+p_0+.684a_0)G_j.
 \tag{LCW.11}
$$

只将 actual cap anchor 槽替换为 (LCW.1)，即可使用

$$
 14.20875k_qH_j+k_fG_j+.018681H_j+.003503042G_j.
 \tag{LCW.12}
$$

原四项、原 signed centers、两 mean、core weak-error columns、
腰的 $g f_0$、世界 $Y_b,K_b$ 和全部 normalization 继续保留。
这不是从旧 error subtotal 减掉一个费用；是对同一个完整公式
使用两个新的、独立已证明的 anchor upper。

配套 [exact reader](../scripts/fourfold_codazzi_local_cap_anchor_saved_bounds.py)
一次完成23个新 Fraction 比较，全部通过，旧科学 target 调用数0。
原 native 未重新生成，全部旧 cumulative records 未重算。
