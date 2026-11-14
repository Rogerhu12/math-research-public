# 本轮 actual common prefix 相对精确桥目标的轴点下界

作者：`/root/numerical_recovery`。结论类型：**精确有理算术证明，待本份独立全文审查**。先前 frozen-target 轴点证明已由独立审者完整复跑，见 `2026-11-10-78718-audit-prefix-axis-lower-v1.md`。这里补上本轮实际生成的尾、精确桥和共同接缝定义；不宣称完整闭曲面或无限尾已经构造。

## 1. 新结论及范围

本轮 `restart8000-02` 的实际共同 prefix 在最终精确桥目标下满足

$$
\|g^{-1/2}(F^*e-g)g^{-1/2}\|_{\rm op}
>7.74147506471938\times10^{-8}>2\times10^{-9}
$$

于一个严格位于接缝修正支撑之外的轴点。这里的十进有理数 $7.74147506471938\times10^{-8}=387073753235969/5000000000000000000000$ 已由独审以 Fraction 严格核为小于报告的精确下界。因此，**任何保留这一个实际 prefix 和所声明最终目标的闭扩张都不能通过原 $2\times10^{-9}$ 门**。这不排除其它频率、其它真实解或同一 $g$ 的精确无限等距构造；不由一个点推断整图的全部几何性质。

实际共同定义为
`notes/2026-11-10-78718-post-restart8000-storage-v2-run-01/closed-map.json`，11,225 B，SHA-256 `6cd427ec5b4642a08ac64e9a1afbc5d4692ad5b449d305ffb10725f606e1eb83`。其 prefix 基底为24个 Cartesian 三倍频模，实际共同基底扩到64，节点6599；扩基仅补零，不能改变支撑外函数。

## 2. 真实生产闭包

下表全部来自实际工具自然返回，未从 guard、mtime 或日志静默推断。

| 阶段 | 真实末工具及 exit | 主要输出 SHA-256 |
|---|---|---|
| own tail export | `9ace36`, 0 | `tail-manifest.json`: `207a40b90ba65e2297c24c48b8d5848d3e18e6ed62ca77024ce71d7b3f68558b` |
| exact radial invariant | `67348b`, 0 | `tail-radial.json`: `de494da5a60a18f5e3735ef7a5a872ee51169923df2b678d04709622557175a3` |
| finite collar check | `a81eb2`, 0 | `tail-collar-check.json`: `93e0aaa0742a5110f936345997609460e8aa8f166a66f9418815370fc1306d85` |
| exact bridge | `024ce0`, 0 | `bridge.json`: `da2c5f8cdfcba8aa68fb535ac981989cb041fab768d674f9037d570f4aa56b47` |
| actual common cut | `a4bdf6`, 0 | `closed-map.json`: `6cd427ec5b4642a08ac64e9a1afbc5d4692ad5b449d305ffb10725f606e1eb83` |

每一步完整 argv、cwd、环境、输入身份、工具回执和闭合文件在同题 `2026-11-10-78718-production-storage-<stage>-01-invocation.json` 与 `-observed-exit.json`；stage 分别为 `tail-export`、`tail-radial`、`tail-collar`、`bridge`、`common-cut`。最后一份观察 SHA 为 `aaad3e13dbbfe579ffab8954f6c60fd2c619b448cafdea52b0f90b4eb9287750`，绑定42个实际闭合文件。新的轴点检查器重新核它们每件的 bytes/SHA，不读活动日志作为证明。

尾的来源是 root 本轮真正成功 CP 自己的 `_tail_0003.json.gz`，SHA `c253eedbf3a4711ad79740d655262a5991e803e38dab2b4a248c386db9efcb7d`。prefix 来源 CP SHA 为 `4776c4c251c4bc6fdadda56aaed78f6fc02175483c5ad3a6fb3cf0359a49cd6a`。没有借用旧 M8/M12/M14 图的误差界。

## 3. 精确点值与接缝支撑

先前已审原程序 `78718-prefix-nodal-axis-lower-v1.py` 从实际 lossless-storage 容器读出原有限 shared-jet Hermite map。每个保存 binary64 数在数学定义中按对应 dyadic rational 解释。它在 native node1518、$\psi=\pi/3$ 得到精确数

$$E=R_\sigma^2+Z_\sigma^2>1,$$

其中 $\sigma\approx0.27472985991302756$ 是旧冻结径向坐标；角向切分量在该轴恒为零。新的检查器在**当前共同定义所引用的同一基底字节**上重新计算该点，逐字比较精确 $E$ 与原节点的有理坐标，未把旧报告数值直接当作输入结论。

共同修正按实际源 `78718-prefix-common-cut-storage-v1.py` 定义。width仍为浮点 `.15`，实际 `searchsorted(mesh, mesh[-1]-.15)` 给 node6124，起点约1.8720381178742067。源只在从此节点开始的 spans 增加 quintic Fourier 修正；全部更早 spans 与一阶节点导数完全保留。1518严格小于6124，故这个点的 $E$ 在实际共同定义中保持不变。零填充到64模也不影响它。

这一步不是“未来若生成共同图”的条件陈述：共同 manifest 已实际产生、实际 producer 已成功构造并检查其端点区间数组，源和输入闭包保持同一身份。它仍只定义共同 prefix 与尾的拼接局部，不因此取得全闭图的其它门。

## 4. 最终目标变换必须带 $\lambda^2$

令旧冻结总长为 $S_0$，最终精确桥定义的总长为 $S_*$，并记

$$\lambda=S_0/S_*>0,\qquad \sigma=\lambda s.$$

最终 prefix 是 $F_*(s,\psi)=F_0(\lambda s,\psi)$。因此对固定 $\psi$ 的径向方向，

$$|\partial_sF_*|^2=\lambda^2E.$$

原 chart 的角变量为 $\theta=\psi-e(\sigma)\sin(3\psi)/3$。在 $\psi=\pi/3$，无论 $e'$ 或径向函数 $a$ 如何，角变量对径向的导数都为零。因此最终目标的这个方向恰有 $g_{ss}=1$。把这个向量代入相对 metric 的 Rayleigh quotient 得

$$\|g^{-1/2}(F_*^*e-g)g^{-1/2}\|_{\rm op}
\ge |\lambda^2E-1|.$$

同一正比例参数变换保留 witness 严格在修正起点之前的关系。

本轮桥给出的精确有理区间是 $[\lambda_-,\lambda_+]$，约为 $1+3.62\times10^{-16}$。检查器用 Fraction 直接计算

$$0<L=\lambda_-^2E-1\le\lambda^2E-1\le\lambda_+^2E-1.$$

报告保存 $L$ 的完整有理数和经过精确比较校验的向下 binary64 显示端点；JSON 的 `lower_display` 对应已验证向下的 binary64 数；其最短 round-trip 十进字符串 `7.741475064719386e-8` 若另解释成精确十进有理数会略高于精确区间，不能直接把该字符串用于严格式。正文按独审真实 `32aec7/ab9c57` 改用严格更小的十进有理数 $7.74147506471938\times10^{-8}$；冻结源与实际报告均不修改。不使用旧值 $E-1$ 原样转移，也不需要全域 target perturbation 上界来证明这一点。

## 5. 程序身份、实际重放与保留的失败

有效源为 `scripts/78718-prefix-common-axis-lower-v2.py`，12,254 B，SHA `8bc77d7c14b68d4c1f13c5c595f227860f4cdefd433afac7606a536293a07e11`。它硬钉原轴点、bridge、lossless reader、共同定义及消费者源；全程0 BVP、0 DN、0 exporter、0 geometry producer。它在临时小文件中完整执行冻结 `db6f-root-exact-bridge.py::main`，检查新鲜证书每字段等于实际桥证书，再使用原有理输出区间。该原桥函数包含根的有理 Taylor 符号、单调性与尺度证明；Decimal只提供种子，并不支付验收。

有效执行真实末工具 `90db74` exit0。报告 `2026-11-10-78718-numerical-common-axis-lower-02.json`，20,806 B，SHA `50c1633e3d42102d0b77f50480e5c81b11c9d9f25d995ec2452a9458b7deebc7`。真实 argv/初始工具/末工具保存在 `2026-11-10-78718-numerical-common-axis-lower-v2-observed.json`，3,097 B，SHA `b59b011a72bab91751118e50e7c7813c675dcc33821dc8ad1b75f96eeec8c7db`。

v1保留为失败历史，SHA `4f656d8d57b8d90b7d02556ced3e09cc002f18b12abd9297d2df08f043bd1550`。其实际 `263567` exit1：原桥把内部 Decimal-seed bracket 向外取256-bit dyadic hull后才输出；v1错误要求在这个不同端点重新算出的 gap 编码与原内部端点的 gap 编码相同。它正确停止，未生成报告或成功结论。v2没有修改原数学源；改为完整原桥证明新鲜重放，避免混同两个不同端点的计算。失败观察另存 `2026-11-10-78718-numerical-common-axis-lower-v1-failure-observed.json`。

## 6. 可直接独跑的命令

所有路径相对本题目录；必须另给全新 `--out`。Python使用同一 primary绝对路径。

```sh
/opt/codex/runtimes/codex-primary-runtime/dependencies/python/bin/python \
  scripts/78718-prefix-common-axis-lower-v2.py \
  --common-map notes/2026-11-10-78718-post-restart8000-storage-v2-run-01/closed-map.json \
  --geometry notes/2026-11-10-78718-post-restart8000-storage-v2-run-01/prefix-base.json \
  --target notes/2026-11-10-78718-post-restart8000-storage-v2-run-01/prefix-target.json \
  --metric-certificate notes/2026-11-10-78718-post-restart8000-storage-v2-run-01/prefix-base-metric.json \
  --tail-manifest notes/2026-11-10-78718-post-restart8000-storage-v2-run-01/tail-manifest.json \
  --bridge notes/2026-11-10-78718-post-restart8000-storage-v2-run-01/bridge.json \
  --point-report notes/2026-11-10-78718-numerical-prefix-axis-lower-01.json \
  --common-observation notes/2026-11-10-78718-production-storage-common-cut-01-observed-exit.json \
  --out notes/REPLACE-WITH-NEW-INDEPENDENT-STEM.json
```

下一数值方向是真正升曲线和速度的共同 Fourier 阶数；不能通过只收紧本图的径向残差或区间上界消除这个精确点下界。
