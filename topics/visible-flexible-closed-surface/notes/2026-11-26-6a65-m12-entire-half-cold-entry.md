# 原 M12 真平接头全半体 Cartesian BVP：背景消费与冷启动入口

2026-11-26，Astra-visible-flex-6a65。**可信度：已执行的有限数值消费与新完整求解入口；全尾求解尚未执行，不能作为精确解或 README 第 5 条的完成证据。**

本入口消费 [R223](../results/R223-m12-common-chart-through-flat-cuff.md) 的同一 $g$ 共同材料图。中央的精确平面曲线、$X_s=e_z,X_{ss}=0$ 与真正平 cuff 的圆周平面两 jet 保持；原 $r=0.6$ common cut 成为内部未知场的一部分。全部 prefix、原 bridge、有限尾和深 collar 使用同一套全局五次 B-spline Cartesian 修正。

## 1. 原完整 prefix 的已取得实跑

公开 run `45797640490`、job `139832301953`、source `8b5358e3` 的 158 元、15,386 列、order 32 / N384 / Gauss6 / LSMR800 单步已由实际独立 Gauss8 / N768 观察得到

$$
7.974019\times10^{-9}\longrightarrow 8.0562388296\times10^{-10}.
$$

这是原固定 $g$ 的真实位置联动下降。LSMR stop 7 表示到迭代上限；训练峰约 $5.16781\times10^{-10}$ 不能替代独立峰。独立新峰在 $s\approx1.961593$，仍位于 bridge 内部；固定的 common cut 是 $S_*\approx2.021775895$。主曲率峰约 $5.11272467855$，实际 J/JT 相对配对误差约 $7.56\times10^{-15}$。完整标量记录见 [该 run 记录](https://github.com/Rogerhu12/math-research-public/blob/2dc56cacb8bc67fd2670fb2962d1503e2b5d7dbd/topics/visible-flexible-closed-surface/notes/2026-11-26-6a65-m12-global-prefix-ci-45797640490-1.json)。

这一次仍固定内部 common cut，故下面释放该接口的完整半体问题是后续实作。它不改变原度量、时间范围或输入振幅。

## 2. 原解析尾背景的真正数值消费

新 `6a65-m12-original-tail-background.py` 使用旧 `FrozenSource` 的同一 160 个精确二进校准常数、解析长度、cap、权函数与原精确 A/B 积分归一化定义。它直接返回

$$
w(r),\qquad w_r(r)=\frac{w_x}{A+\alpha B},\qquad
D(r)=\int_r^{c}w(\rho)\,d\rho.
$$

它没有对数值 $w$ 包多项式求导来代替 $w_r$，也没有把一个包的中点定义成新度量。

第一版盲 Gauss 自适应给出 $\alpha\approx97.64534740814844894$，落在原已证明的严格 $\alpha$ 盒之外，**未采用**。具体原因是 cell 5 / 6 靠 source 端点的极窄 $|w_x|$ 小瓣未被两套 Gauss 探针察觉。该程序虽返回 exit 0，不能据此声称源身份核验通过。

修正直接消费旧 `db6f-audit-inner-warp-variation.py` 已审的稳定转向点公式。若 uncapped log slope 为 $C+J S(x)-\lambda x$，且 $J>0$、$15J/8>\lambda$，设置

$$
z=\sqrt{\lambda/(30J)},\qquad x_- = \frac{2z}{1+\sqrt{1-4z}},\qquad x_+=1-x_-.
$$

在这些真实转向点预先分割，再作数值积分。这里没有重证或改写旧 variation 结论。新消费器还把原严格 $\alpha$ 盒作为硬性拒绝条件，并核对其校准表 SHA。

两档实际完整计算都返回 exit 0：

| 数值积分细化参数 | profile 数 | 叶数 | $\alpha$ 数值 | 耗时 |
|---|---:|---:|---:|---:|
| $2\times10^{-18}$ | 1440 | 12404 | 97.645347407779752975 | 4.351400566 s |
| $5\times10^{-19}$ | 1440 | 12435 | 97.645347407779752975 | 4.124317392 s |

两档都位于原严格 $\alpha$ 盒；有限背景高度数值为 $0.049281104169724834997$。9 个真实物理半径逆像的 $w,w_r,D$ 一致到约 $10^{-19}$；包括 cut、cell 0 的强变化区、有限尾和深 collar。先前 486 个 profile 点的解析公式实现核对也全部落入原区间公式的包含盒。

上述 Gauss 差值与两档一致性都是数值核对，**不是严格积分余项证明**。保护层 160 以下原无限背景的高度贡献仍属于原数学定义；它没有被数学上截成零，数值报表明确未把该极小无限项纳入显示值。

当前背景源 SHA256：

`cab284d7506523dbe56a2711a654764084ef0a5d253187bafcec965ca06da1dd`。

本地可重生报告只留临时文件；对应 SHA256：

- 未采用的第一版报告：`f1953cca3058476ec1170eefa767f73926a75595501a400daa464e9bf650b3e2`。
- 修正后第一档：`fe9ea365f63d904652fc0fcca255dd37cde92b876b80b9437c9952ab05d42ad6`。
- 修正后第二档：`c62b1791721af26a8af2cc6458b05e33076b014d2241e594360c2f24fcfdede0`。

## 3. 原积分尾的精确有理查询

`6a65-m12-stream-tail-query-cache.py` 流式读取原 24 个历史 Git blobs，逐块核对 Git framing、清单字节数、SHA256 和共享行。对每个指定物理半径，使用原精确归一化径向增量及 `Fraction` 算术计算同一扰动系数的 value / first / second jets；最后才转换成数值求值缓存。

径向跨内的四次导数、多项式积分与实际二阶导数来自同一多项式。真深 collar 使用原 quintic C² 接法；不是另拟一条曲线。缓存不定义查询点之间的新插值场，原连续场始终由原源定义。

当前该新 streamer 已通过一个独立给定有理四次多项式在六个半径点的完整 value / first / second 精确相等核对，exit 0。**本轮尚未对所有 24 块执行它的新多点路径。** 原单 endpoint 的完整 24 块流式计算已在前一结论实际完成，不能冒充这个新路径的执行记录。

### 原末块的实际接口核对

新 `6a65-m12-entire-half-interface-check.py` 又实际只恢复最后一个 1,787,305-byte 原块，Git blob 为 `1a9cce86c3ad6e88bc07dedb465a08066a62a5ab`，SHA256 为 `89fe80d3453aa25978c343f7d58d51a31dd1d3fe37e6fffcdd48cfc31b551249`。最后两个相邻 span 的全部 141 个系数，在六个有理局部位置上核查：左右一、二阶端迹、中点一阶值、精确积分与跨 span 的 value / first / second 一致性，所有差均严格等于有理数零。

这项小核对把最左局部 value 取为原显示行的值；它不冒充尚未恢复的全尾累计 value。使用该同一局部 primitive、真正原末端导数和实际中央材料角图，N768 上的直接 Cartesian 与独立柱坐标六 jet 公式最大分量差为 $2.23\times10^{-16}$；完整归一化 Gram 的最大差为 $5.55\times10^{-16}$。整项 exit 0，7.164550590 s，真 cut 的精确有理查询 key 回程也通过。

同一次原末端数据还给出一个严格但仅针对固定原 cut 端迹的见证。令 $A$ 为原 planar $F_r$ 系数之和、$B$ 为原 height $F_r$ 系数之和。在 $u=0$，原 $w(c)=1/2$、$r_s=-2/\sqrt5$，因此

$$
|X_s|^2-1=\frac45\left((1+A)^2+(1/2+B)^2\right)-1
=\frac{15348436479357175141899431703175496874609}{30649910817317777167166940543006183672374782443672043520}
\approx5.007661056777045\times10^{-16}>0.
$$

所有系数都是原二进数的精确有理值，故这是固定该完整一阶端迹的消费器不能成为精确等距解的具体理由。它比当前独立 prefix 峰小约六个数量级，不能据此反对真实空间加密；全半体入口已经释放这个内部 cut，不受该固定端迹限制。

## 4. 全半体真实准备与完整残差

`6a65-m12-entire-half-cartesian-bvp.py prepare` 已实际执行，exit 0，8.878701872 s。固定原 $g$ 下，设置 prefix 80、tail 64、源接口至 depth 12、order32、N384、Gauss6，得到：

- 362 个实际径向元，35,378 个 Cartesian 未知数；
- 2172 个训练径点及 2896 个独立 Gauss8 径点；
- 2859 个需要从原尾精确恢复的不同物理半径；
- 真 cuff 为原二进实数 $2702159776422297/18014398509481984$；
- 原 $r=0.6$ common cut 没有固定修正端迹。

prepare 的 grid SHA256 为 `d5adf34244e5509ce580a42592b2028e15ed80451caf72d281a4f17a8526f564`；query recipe SHA256 为 `1fa91973c3a9665319c50a522838535903a8de12d75317a35f503a4bdca8253e`。这些可重算数组只留临时目录，不提交。

完整位置读取器在 prefix 消费原精确 common-cut map；在尾消费同一 Fourier 扰动、真实 $w,w_r,D$、原反射方向和原高度规。所有六个位置 jets 按 R223 的完整链式公式生成。J/JT、非线性接受检查和独立观察均使用完整实际 Gram；$H_1$ 带状预条件不改变零集。独立观察固定为当前径向 Gauss 阶加 2、角节点数加倍。

## 5. 冷启动命令与发布边界

在公开 Actions 的 `$RUNNER_TEMP` 下先按已登记公共 Git blob `26ce0426c60ef868c53597a82252e0559c1cc21e` 恢复原 prefix 文件并核 SHA，然后可运行：

```bash
python topics/visible-flexible-closed-surface/scripts/6a65-m12-entire-half-cold-run.py \
  --data "$M12_COLD_DIR/m12-prefix-data.npz.gz" \
  --directory "$M12_COLD_DIR/entire-half" \
  --prefix-elements 80 --tail-elements 64 --tail-depth 12 \
  --order 32 --angular 384 --gauss 6 --iterations 800 --newton 1
```

此顺序入口执行 prepare、精确尾查询、完整半体 solve。它不自行发布 Git、artifact 或 Release；上层 workflow 只记录小标量与 SHA，并按根 README 执行 pull/rebase、双 README 差异检查与普通推送。原 source、参数和全部历史 blob 身份足以重新生成临时场。

新四脚本当前 SHA256：

| 脚本 | SHA256 |
|---|---|
| `6a65-m12-original-tail-background.py` | `cab284d7506523dbe56a2711a654764084ef0a5d253187bafcec965ca06da1dd` |
| `6a65-m12-stream-tail-query-cache.py` | `81385a77c04895c69ae23650af5874f2c385a736e3aa667b95292928c17a6788` |
| `6a65-m12-entire-half-cartesian-bvp.py` | `7214054f65bfbd1055122dddf235074bc812c88cdf5d418b630877bf8b21880b` |
| `6a65-m12-entire-half-cold-run.py` | `d5f0c967bbec9cd45382afdde8418d974635af734d6fa4aa98aab1d0a0d41f3d` |

小接口检查源码 SHA256 为 `4dbe157da39d8c6d477f906114d982075273379291818f2295ba6b033274e7b3`。冷启动调度器仅给精确 blob 恢复子进程保留 `M12_RECOVERY_TOKEN`；数值 prepare 与 solve 子进程的环境明确剥离该变量。独立 whole-half workflow 的狭窄 push 请求路径位于本题 `ci-requests/`，只发布标量结果和身份回执；其所有 8 个 shell 段、5 个嵌入 Python 段与 5 个新 Python 源的语法核对均返回 exit 0。

本记录时，完整半体 solve 尚未实跑；没有全域新误差、reach 或时间族的合格结论。下一实际工作就是消费这 2859 个原尾查询并执行完整同 $g$ 求解，随后在同一几何下继续空间、求解与独立观察加密。
