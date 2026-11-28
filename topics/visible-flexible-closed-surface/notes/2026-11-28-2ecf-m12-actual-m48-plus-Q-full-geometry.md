# 同一原 g 的实际 M48+Q：独立源、完整几何转移与 G12 准确接口

**已完成的新消费：** 对实际 M48 保存系数 `6aafee941eefdada991efa93316f89f9ddbdcd57f05c8bf33a51d19fe74e3d61`，保持该 W 不变，定义新的完整物理族

\[
Y_t=X_t+C_t+Q_t+W_t.
\]

这里 Q 是 R250 的准确全有限尾修正，原目标 g、材料参数和全部相位范围不变。本条实际核对该场自身的 R249、R253 和完整 cross-Gram 回执，再支付 Q 的全部连续六 jet，得到全空间、全相位的 metric < 9.963071e−7、reach/D > .0311647758481、held/D > .0527831170810，以及含反射的严格非全等。通用消费者实际自然返回 0，全部有理门槛成立。

新源已在真实 G12 的 13,731 个准确查询半径上生成独立缓存，含完整 141 通道和 0/1/2 径向导数。本条**没有**运行 Q 源上的新非线性步，没有把原 M48 solver 回执改称 Q 源回执，也没有把旧数值残差改标为新图残差。README 第 5 条没有因此完成。本条不新生 Q 源的 STL。

## 1. 两种身份及实际输入

保存的 W 仍是原 M48 的 736×146 个 binary64 系数，完整径向 knot 和全部角模不变；其内部重复 knot 至多 3，五次修正全局至少 C2。原 solver 的数学源始终是 X+C，其已执行的数值步骤与独立观察数据仍只属于原源。新物理映射 Y 由准确函数 Q 的加法另行定义。

原 X 仍由以下固定输入决定：

| 原准确输入 | SHA256 |
|---|---|
| prefix data | `359d491cd592962d467fdd538013977ee9a92070346de41c227d9ca3e1ef3bd0` |
| common-cut meta | `253179d585d4ac0e59206d4e579de5663943f126473668c45a3bbda665c9c8f2` |
| exact bridge | `1389cf1a339b0a0d749beb666b6def24a31e766eff0abf63289217728ceacdaa` |
| 完整 M12 manifest | `cc23977e25a09c34db91723dd784cab4b18b89e325fc2ca2fb8dd7ee6866a104` |

Q 沿用 R250 的 24 个原块、18,552 个 span、18,551 个内部节点和 141 通道；平滑半宽固定为相邻准确 span 长度最小值的 1/64。准确 jump/window stream 为 `a64d212afa7bdd19599ff8da5d0ecdd82b5ed940b8cbb6f7a9e1d878b965b5d7`，没有重新选择或缩小构造参数以压低残差。

本次实际读取并核对的同场输入如下。表中每份连续回执都必须指向同一个实际 field、grid 和原 solver result；不能借较早 M32 场的几何。

| 实际 M48 输入 | SHA256 |
|---|---|
| field | `6aafee941eefdada991efa93316f89f9ddbdcd57f05c8bf33a51d19fe74e3d61` |
| grid | `5f366284b435c8911fa1bddcc9bef4cc92c646f06730a959bd4c773b4c3cd7cd` |
| 原 Q-free solver result | `c0ca3ce3832b12c188dca87218d87639cbe266c27c129323505ad1d12225b9c2` |
| R226 correction receipt | `565a8a5b49e3352cbf09cb5f0bfed4cd0c37ea8348cc1299d46256979bd57d0d` |
| R230 原源 CX receipt | `3b7c5eeb532c08e7be10f0a3bdce70e739f15316bd8fa264eaaa7b287db483b2` |
| R249 本场完整二 jet | `47720443469edede69e9b583d9fdd4d4f7006182170dfe98c04f3dd9e66a2f93` |
| R253 本场分区法向转移 | `be40e6c9f02c5b3f0c1d0e0cbce79aaa52204d52555ea55316ef134d6db622bf` |
| 本场完整 v4 cross-Gram | `da4cdc5c98c68aca4f82433b0672ea6fdbb0a31fada016676ca6dc13963e5f7e` |
| 原 solver 查询 report | `7d75c93355fb5b79077c8b606294487c02f591e70e40111cac97abcf924da6d2` |
| 原 solver 查询 cache | `a98098ed40ffed92cae3f3ca208c91456d8a7f4958b08c4a21973c79dd881c1b` |
| R250 完整 Q 连续 report | `7c52dc85926d8e9ea8583ca33380ea7b7cf8f6cd2672e4eb2847e3548d65c426` |

本条生成的数学候选身份为

`e81f3ecf589da8d776b7a9974dc1750b4a4fdb936ff5729dc1ece0afce01f30a`。

该身份把原 data/meta/bridge/manifest、保存的 W、实际 grid、准确 Q 的 producer、divisor 和 jump stream 一起规范化哈希。有限查询缓存的密度不决定数学图，因此后续增加查询无需改数学候选身份；每份实际缓存仍有其独立 SHA。

## 2. 适用于任意合格实际场的转移公式

以下推导并不硬编码 M48 的系数。输入任意一份同源实际保存 W，要求它自己的完整 R249、R253 与 cross-Gram 回执通过身份及覆盖核验。设

\[
\eta_0\ge\|C+W\|_\infty,\quad
p_0\ge\|D(C+W)\|_{g,\infty},\quad
c_0\ge\|D^2(C+W)\|_{g,\mathrm{coord},\infty},
\]

其中最后一项是 R249 已证的目标缩放二阶坐标 jet 和。R253 另给完整 prefix 上的一阶界 pP≤p0，原源的分区二 jet 界为 CXP、CXT。设本实际 Q-free 场全域度量误差的已证上界为 ε0。

令 R250 物理 (s,u) 六 jet 界依次为 B0、Bs、Bu、Bss、Bsu、Buu，有限尾最小准确半径为 r0。设

\[
\eta_Q=B_0,\qquad p_Q=B_s+B_u/r_0,\qquad
c_Q=B_{ss}+2B_{su}/r_0+B_{uu}/r_0^2.
\tag{1}
\]

R250 的物理界已包含 |rs|≤1、|rss|≤6 的完整链式项，不能把源的 r 当作弧长，也不能省略中央计算角到真实材料 u 的导数。整个 Q 支撑在原有限尾内部，故在完整 prefix、中央接缝、deep collar、真实 cuff 与固定帽上恒零；在每个原有限尾节点上两 jets 全零。

### 2.1 同一 g 的完整 Gram

旧图 Z=X+C+W 的目标标架微分满足 ||DZ||₂≤√(1+ε0)≤1+ε0。完整 Gram 恒等式直接给

\[
\|(Z+Q)^*e-g\|_g
\le \epsilon_0+2(1+\epsilon_0)p_Q+p_Q^2=:\epsilon_1.
\tag{2}
\]

这里消费的是该实际 Z 自己的 ε0，不能用原 X 的缺陷替换。式 (2) 在整个有限尾和全部角度成立，Q 支撑外仍沿用旧完整证书。原相位同时作用于 Z 与 Q，保持相关范数，所以同一个界覆盖整个 t 区间。

### 2.2 全同伦与分区曲率

相对 R21 的原图 X，新的总改动是 C+W+Q。记

\[
\eta=\eta_0+\eta_Q,\quad p=p_0+p_Q,\quad
d_0=257212/10^{13},
\]

\[
K_0=4763997235009095/562949953421312,\quad
R=2131902881202937/1125899906842624,
\]

\[
d_*=d_0+2(1+d_0)p+p^2,\qquad
\nu(v)=\frac{3v+v^2}{1-d_0}.
\tag{3}
\]

这些界共同控制整个线性同伦 X+v(C+W+Q)，0≤v≤1。原 X 的 CXP、CXT 保持原值；Q 被计为改动，未把新源 Hessian 静默替换成旧源 Hessian。由于 Q 在 prefix 恒零，分区曲率可取

\[
K_P=\frac{K_0(1+d_0)+\nu(p_P)C_{XP}+c_0}{1-d_*},
\qquad
K_T=\frac{K_0(1+d_0)+\nu(p)C_{XT}+c_0+c_Q}{1-d_*},
\]

\[
K_* = \max\{K_0,K_P,K_T\}.
\tag{4}
\]

R253 的 prefix 选择已经覆盖真实 prefix 边界不确定性；本条只使用其已证 sup。没有以某个浮点边界把 Q 漏算进 prefix。c0 本来是全域界，在 prefix 用它仍合法；给 tail 添加完整 cQ 即覆盖其全部支撑。

还取

\[
D_*=2(R+\eta),\qquad
\sigma=.737-1.9\nu(p)-\eta.
\tag{5}
\]

消费者准确检查 d*<1、η<1/K0、R+η<2、σ>1/K*、K*<2000。由原 R10 完整正支持法管论证，得到全同伦、全相位的闭嵌入与全点对 reach≥1/K*；不是只凭主曲率排除远处自接近。

固定帽及其标记完全不动，故原握持见证与固定帽尺寸给

\[
\frac{\delta_{\rm hold}}D\ge
\frac{.19989114-2\eta}{D_*},\qquad
\frac{\operatorname{diam}H}D\ge\frac{3.5426}{D_*}.
\tag{6}
\]

活动三阶矩的损失仍至多 2400η(1+9η)²；本次准确验证它小于 .44016。原 D3、环境反射结构和固定帽标记保留，R16 遂给 δE>0，刚体群包含反射。所有量均按整个 F0(M) 的直径 D 归一；D* 是其上界，因此使用 D* 的下界是保守的。

## 3. 本次实际有理结果

R250 全域准确 Q 给

\[
p_Q<1.591280\times10^{-12},\qquad
c_Q<.000647425740.
\]

本场的 c0 约 .004841523192702385，pP 约 3.932267236856117e−7。Q 的二 jet 只增加 tail 的预算；计算后 KP 仍是最坏项，KT 约 8.470054141593096，低于 KP。以下显示值已向安全方向放宽，机器证书使用 report 中的准确有理数字段。

| 新物理族 Y 的全域全时量 | 严格界 |
|---|---:|
| 同一原 g 的最大相对度量误差 | < 9.963071e−7 |
| 完整同伦的粗度量上界 d* | < 4.227745e−5 |
| 总位移 η | < 1.928313e−7 |
| 全域目标一阶改动 p | < 2.112564e−5 |
| prefix 缩放二阶改动 | < .004841524 |
| tail 缩放二阶改动 | < .005488949 |
| prefix 曲率上界 KP | < 8.473021711 |
| tail 曲率上界 KT | < 8.470054142 |
| 整个直径统一上界 D* | < 3.787020650 |
| 正支持 σ | > .7368793901782 |
| 全相位 reach/D | > .0311647758481 |
| held/D | > .0527831170810 |
| 固定帽直径/D | > .9354583266799 |
| 活动三阶矩损失 | < .000462796596 |
| 含反射的 δE | > 0 |

通用源 `2ecf-m12-smooth-actual-field-geometry-transfer.py` SHA256 为

`d9238f8dbee0aa9a33d95753d32fcadd5ed175b548356a56b380a8c9f3c16af7`。

本次自然退出 0，内部用时 .158069531 秒，含 Python 导入的整个进程峰 RSS 为 32,204 KiB。完整准确输出 `m48-plus-Q-all-phase-geometry.json` 为 30,384 bytes，SHA256 为

`404f673898120838c1d34032ca25165683fed7b29b0b471a08bd042446000e9a`。

消费者固定验证已证明 producer 的代码 SHA，读取实际保存的系数、完整模式和 knot，检查 C2 重数与端点两 jets；逐项交叉核验完整几何、完整度量、原源和 Q 接口的输入身份。它没有把一个任意新增 JSON 上的 `true` 当作新的证明。

## 4. 真实 G12 查询上的独立准确源

为了使新数学源可被后继更密的生产接口消费，本次对已经实际生成的 G12 原查询集合重算准确 Q，未替换活动原源。原 4,631 查询及新增 8,554 查询合为 13,185 行，加上 546 个诊断半径，合计 13,731 个不同准确半径。

R250 的同一个 flat-switch 消费者用 Fraction 处理真实半径和窗口，并用 256-bit 向外区间计算指数及两阶导数。325 个平滑窗口与查询相交，138 个半径恰为原节点、814 个是窗口内非节点查询；全部查询和完整模式均被覆盖。该准确查询执行自然返回 0，用时 62.339861118 秒，整个进程峰 RSS 为 310,996 KiB。

实际 longdouble 合并自然返回 0，用时 7.845410535 秒，峰 RSS 为 409,968 KiB。814/13,185 个原源查询行加入非零 Q 存储值，共 343,750 个系数；546 个诊断行全部保持不变。准确端点、共同切口两 jets、完整模式和其余查询元数据按原合并规则保持；本次几何消费者又独立比较了原 solver、G12 base 和新源的端点/模式数组与新旧 G12 查询半径。

| G12 接口输入/输出 | SHA256 |
|---|---|
| 原 G12 查询 report | `1a222405e67641f5968c3bca36d50e372356ddc9508aeaf25e2267e51b0a698d` |
| 原 G12 查询 cache | `8c95cfeb3c5ebd186cf299d449d0835d718900c947669a8a862de6d68ff4eacf` |
| 准确 Q 查询 report | `60b485d8998b586f6fd263ef648bd6d3d84a455661ee6248454bee3828285396` |
| 准确 Q 查询 cache | `850f54db2a836cfdd33af4cbac4e32b700c80874d599e362eda3e7d047dc5202` |
| interval query stream | `464f633dd89e931563b4930d7c3960c15735cc5fabe055aa2bf24c0cd618f759` |
| 独立 X+C+Q source report | `f55486e4a748a3978c23f24e1553762b24d289e35e304ec4eda2d250979b0559` |
| 独立 X+C+Q source cache | `baff6aab2e3b89fde5c9c1b47751269e4ef1a9e8cc5666c4753f8b180e31ec4c` |

此 G12 runtime source 的 recipe 与原 M48 solver recipe 不同，但固定数学 X 和 g 相同。消费者同时记录两种 recipe，不宣称 M48 的已运行 solver 曾消费 G12+Q。

### 查询误差的准确范围

以下误差覆盖全部 13,731 半径和完整角 Fourier 和。第三列的参照对象是“原已存储源 + 准确 Q”，包括实际 longdouble 加法误差；原源自己的既有求值误差、运行时三角函数和最终 packet 转 float 的误差仍须另付。

| 物理 jet | Q 准确查询/存储误差上界 | 合并后新增总误差上界 |
|---|---:|---:|
| Q | < 7.212420e−42 | < 7.169483e−24 |
| Qs | < 5.275201e−35 | < 4.936474e−22 |
| Qu | < 4.766524e−41 | < 2.074237e−23 |
| Qss | < 3.449824e−27 | < 1.624028e−19 |
| Qsu | < 8.917003e−34 | < 1.453187e−21 |
| Quu | < 1.389213e−39 | < 8.375442e−23 |

Q 查询报告还给出这些实际查询圆上准确 Q 自身的完整角一阶界。从其 `sampled_exact_Q_native_six_jet_upper` 作准确有理组合得到

\[
\sup_{r\in\mathcal R_{G12},u}\|DQ\|_g
<3.387783\times10^{-15}.
\]

将同一个 W 保持不变时，在这些查询圆上由 (2) 的交叉项公式，真实 Gram 的变化不超过 6.775573e−15。这是有限径向集合、全角的准确增量界；它不被外推为全域界，第一至第三节的完整证明始终使用 R250 较大的全域 pQ。该数值也没有被用来虚报任何尚未执行的新残差下降。

## 5. 复现接口与范围

先按 R250 准确 Q 查询与合并脚本对真实目标查询 recipe 生成独立 source。下面的所有输入均由前述已固定 producer 生成；路径仅示意 Git 外重生目录。

```bash
python scripts/2ecf-m12-smooth-actual-field-geometry-transfer.py \
  --scripts scripts \
  --data "$SCRATCH/m12-prefix-data.npz.gz" \
  --field "$SCRATCH/m48/result.json.field.npz" \
  --grid "$SCRATCH/m48/grid.json" \
  --result "$SCRATCH/m48/result.json" \
  --query-report "$SCRATCH/h487/entire-half-exact-tail-queries.json" \
  --query-cache "$SCRATCH/h487/entire-half-exact-tail-queries.json.npz" \
  --source-bounds "$SCRATCH/h487/entire-half-original-source-bounds.json" \
  --correction-bounds "$SCRATCH/m48/correction-bounds.json" \
  --two-jet-report "$SCRATCH/m48-local-material.json" \
  --regional-report "$SCRATCH/m48-regional-geometry.json" \
  --continuous-metric "$SCRATCH/m48-full-cross-local.json" \
  --smoothing-report "$SCRATCH/smooth-full-div64.json" \
  --regularized-base-report "$SCRATCH/g12/exact-tail-queries.json" \
  --regularized-base-cache "$SCRATCH/g12/exact-tail-queries.json.npz" \
  --Q-query-report "$SCRATCH/g12-smooth-source-queries.json" \
  --Q-query-cache "$SCRATCH/g12-smooth-source-queries.json.npz" \
  --regularized-report "$SCRATCH/g12-regularized-source.json" \
  --regularized-cache "$SCRATCH/g12-regularized-source.json.npz" \
  --out "$SCRATCH/m48-plus-Q-all-phase-geometry.json"
```

本条没有把全图正则性提升成 C∞：原有限尾的多项式源内部已被规整，但原背景接口及实际 W 的 triple knots 仍按全球 C2 使用。原相位保持、固定帽保持与所有上述几何均已覆盖；精确等距存在、Q 源新 Newton 接受及同 g 的真实加密至机器/求解容差仍须由后继实际工作完成。

所有可重算 raw、Q cache、merged cache 和完整有理报告只保留在 Git 外。提交内容为此说明与通用消费者源码，未发布任何大数组或以旧场网格替代新 Q 场网格。
