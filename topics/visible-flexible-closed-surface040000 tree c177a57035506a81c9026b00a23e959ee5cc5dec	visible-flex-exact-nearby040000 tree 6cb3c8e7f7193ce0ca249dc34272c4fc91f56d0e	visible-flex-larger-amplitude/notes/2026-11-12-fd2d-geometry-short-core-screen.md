# 新 cuff 的短活动核设计记录

2026-11-12，constructive_geometry。这里的线性计算不是新的非线性共同 g 解，
也不是当前 M15/W22 的 fixed-g 加密。固定帽的完整证明分别在 R111、R113；活动核仍缺。

## 新 .32 cuff 的物理有限端口

第一套输入从 `closing_weighted_candidate_v3_k6_width045_config.json` 复制，
仅在独立设计文件把 `width` 由 .45 改为 .28、`spacing` 改为 2。
没有修改生产输入或借用旧物理 DN。

`notes/2026-11-12-fd2d-short-core-cuff032-config.json` 的 cut 为 r=.6、w=.5，
curvatureBound=6，cuff=.32。调用

```bash
CLOSING_TAIL_CACHE="$PWD/topics/visible-flexible-closed-surface/repro/source-root/topics/large-amplitude-twist-flex/scripts" \
node topics/visible-flexible-closed-surface/scripts/950f-tail-linear-cusp.mjs \
  topics/visible-flexible-closed-surface/notes/2026-11-12-fd2d-short-core-cuff032-config.json \
  topics/visible-flexible-closed-surface/notes/2026-11-12-fd2d-short-core-cuff032-port.json 2 256 48
```

自然退出 0。实际生成的有限背景有 alpha=1.5036895129937504、最小 warp 宽度 .27422535149772875、
heightSpan=.04270967152659698。选定 far=48 的理想远线，逐真实 profile 的 cusp-split RK4 每段 256 步，得到

| 模态 | cut 高度 DN 斜率 |
|---|---:|
| 2 | -5.568396582960965 |
| 4 | 15.891863046687671 |

这些是实际有限重排 profile 的线性结果；没有无限深远端误差界或非线性 DN 结论。
R111 第二方案的 cuff 高度 .5247193847727812，扣掉该旋转背景高度后剩约 .4820097132461842。

## 只压低旋转背景高度不够

`scripts/fd2d_short_core_screen.py` 构造一个明确 C² 前缀：先从母线角 0 外张到 pplus，
再转向 -pdown，随后保持径向速度，最后用二次角函数刹车到实际 cut 的角和二阶 jet。
转向的角速度使用两端宽 .08 的三次 smoothstep，内部为常数，故角及角速度在接点连续。
背景满足

\[
a'=\sin\phi,\qquad z'=\cos\phi,
\]

从而与新 cut 的 r、w、w_r 精确地定义同一套前缀端 jet。数值积分另有离散误差。
对于单模态 m，传播的是

\[
\frac d{ds}\begin{pmatrix}f\\g\end{pmatrix}
=\frac1a
\begin{pmatrix}-(m^2-1)v&-m^2b\\
(m^2-1)v^2/b&m^2v\end{pmatrix}\begin{pmatrix}f\\g\end{pmatrix},
\quad v=a',\quad b=\sqrt{1-v^2}.
\]

核心线为 (f,g)=(1,0)；实际端口给目标方向
\((-w(rD_m-m^2)/(m^2-1),1)\)。代码对这一有限线性方向求根。

完成的 12 个共振候选都记录在 `notes/2026-11-12-fd2d-short-core-screen.json`。
例如 (pplus,pdown,Kout,Kturn)=(1.3613976507007104,1.56,10,10) 的方向残差约 1.22e-10，
包括尾的背景高度只有 .3859143682865359，末端高度模的增益约 -.0099565250。

但完整一阶 XYZ 模型

\[
X=(a+qf\cos2\theta)e_r-\frac{qf}{2}\sin2\theta\,e_\theta
 +(z+qg\cos2\theta)e_z
\]

在 q=.3 时已经给高度峰 .5466276298259616、y 上界约 1.1223854，
而中央见证点 (0,1.3,0) 到这一模型的最近距离仅约 .1776215。
其他 11 个候选同样没有通过 R111 的完整窄板和握持保护筛选。
所以低背景高度和线性共振本身不够，不能采用这些候选申报强比例。
该一阶模型有 O(q²) 的固有度量缺陷，且有限 q 时不是准确支撑核；
这些数据只筛选设计，不能据此宣称真实非线性曲面不存在或已通过。

复现保存的参数只需给 `--replay`；不加该参数会重新执行注明的 12 组粗扫描。

```bash
python topics/visible-flexible-closed-surface/scripts/fd2d_short_core_screen.py \
  --port topics/visible-flexible-closed-surface/notes/2026-11-12-fd2d-short-core-cuff032-port.json \
  --replay topics/visible-flexible-closed-surface/notes/2026-11-12-fd2d-short-core-screen.json \
  --out /tmp/fd2d-short-core-replay.json
```

## 椭圆高接口的新短尾

R113 使新的实际固定帽允许活动核高度约 1.288641，而不是 .525。
为了把这个高度主要留给活动前缀，第二套独立输入取
cut r=.4、w=.1、cuff=.32、width=.08、curvatureBound=7；
同时将 slopeCap、pulseCaps、valleyCaps 乘以 .2，其余有限 source 参数保持所记录值。
文件是 `notes/2026-11-12-fd2d-ellipse-cuff032-cut04-config.json`。

同一物理线性脚本以 4 个模态、每段 256 步、far=48 实际运行，自然退出 0，
输出 `notes/2026-11-12-fd2d-ellipse-cuff032-cut04-port.json`：

| 量 | 数值 |
|---|---:|
| alpha | 7.717139914377993 |
| 最小 warp 宽度 | .05003137469782325 |
| 背景经线长度 | .08005605867123879 |
| 背景高度 | .001912377540106331 |
| m2 DN | 7.657720764629502 |
| m4 DN | 32.03323279508542 |
| m6 DN | 58.32248642397737 |
| m8 DN | 85.11270532016188 |

该短尾给真实正的有限归一参数和很小的背景高度。
它没有继承旧尾的非线性解、全时 reach 或无限 collar 的闭合认证。
后续前缀求解应使用这套实际端口，并同时支付活动体窄板、见证球避让和 reach；
不再只最小化旋转背景高度。
