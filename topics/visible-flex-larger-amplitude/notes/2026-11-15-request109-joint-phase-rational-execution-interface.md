# Request109：R280 三个条件有理案例的最小公开执行

2026-11-15。此请求是在 R280 证明与源已完成之后的独立算术执行配方；R280 登记不等待该执行。没有当前曲面输入，没有 BVP、native、ODE、RHS、J 或闭场重算。

## 1. 唯一入口与冻结身份

| 文件 | 字节数 | SHA-256 |
|---|---:|---|
| public-joint-phase-normal-balls-request.json | 5053 | 1899a66371506abb558fa166cf92f9657b1935fb3c1b45658cf2e3aa7ae60e30 |
| visible-larger-public-joint-phase-normal-balls.yml | 9209 | c5d92273c4bf5f105841c194b9b761e4e585a39026304bfafecf2d167cb00948 |

workflow 放 .github/workflows/；request 放 topics/visible-flex-larger-amplitude/computations/。唯一 push trigger 正是该 computations request 路径，concurrency 为 visible-larger-r280-joint-phase-normal-balls，cancel-in-progress=false。

科学源码闭包仅两件：

- geometry_20261115_joint_phase_normal_balls.py：8454 B，SHA c5548f28bfe56a283403a7d16e1879c1c1243d0a0bc80761586fe50e1aec1466；
- 冻结 root_mixed_phase_normal_balls.py：9012 B，SHA ecea0ef58aa5755270807596da5512552ac52fab27e90492fcf85fab095716c6。

新源在执行前要求 GITHUB_ACTIONS=true 且 GITHUB_REPOSITORY=Rogerhu12/math-research-public。原 R62 源不改，不读取其旧输入或旧结果文件。

证明身份是 R280-joint-endpoint-all-phase-normal-balls-and-finite-cover.md，19219 B，SHA 6d32cd819d19adeb721780c692100d59a2d361a19f8274f60394a548c3a30aab。workflow 不把该证明是否已获单独审查作为运行门。

## 2. 三个新输入及解析预期

所有坐标和半径均为整数或准确有理字符串。这里的预期来自下述解析恒等式，尚不是实际运行结果。

| 案例 | 输入要点 | 解析预期 |
|---|---|---|
| joint-strict-extension | $p_0=(1,0,0)$，$q_0=(1/2,0,0)$；$n_0=(1,0,0)$，$m_0=(0,1,0)$；四半径为0，$\tau=1/3$ | 两个旧单端均失败；新联合通过；最终 OR 通过 |
| old-endpoint-retained-when-joint-fails | $p_0=0$，$q_0=(1,0,0)$；$n_0=(0,0,1)$，$m_0=(1,0,0)$；仅固定端法向半径为2，其他半径0，$\tau=1$ | 移动端旧门通过、联合门失败；最终 OR 仍通过 |
| phase-pi-equality-is-not-a-strict-pass | $p_0=(1,0,0)$，$q_0=(-1,0,0)$；$n_0=(1,0,0)$，$m_0=(0,1,0)$；四半径0，$\tau=1$ | 旧门和联合门均严格拒绝；不能遗漏π等号 |

第一例正是证明 §280.4 的严格新增配置，令 $c=\cos\phi$：

$$
J(\phi)=\tfrac34(c-\tfrac23)^2+\tfrac16,\qquad
\mathcal J(t)=\tfrac14-\tfrac12t^2+\tfrac94t^4.
$$

第二例的中心弦恒为 $(1,0,0)$，$D_c=1$。移动端 $G_n=1$，固定端预算 $b_m=2$ 且其叉积为0，所以 $G_m=-4$，$J=-3$。这精确测试保留旧门的 OR；若错误地用联合门替换旧门，会丢掉该成功案例。法向半径2仍是一个可以包含单位法向的合法条件输入，没有虚构更强包围。

第三例有

$$
G_n(\phi)=\sin^2\phi,\qquad
G_m(\phi)=(1+\cos\phi)^2,\qquad
J(\phi)=2(1+\cos\phi).
$$

半角多项式为 $\mathcal J(t)=4+4t^2$，对每个有限实数严格正且没有实根，但 $J(\pi)=0$。因此必须由显式π端点检查拒绝。这不是浮点近似等号或容差测试。

三例的旧整圆距离门都不通过；执行不会因距离分离而跳过所测联合行为。它们是条件点对输入，不被宣称属于当前完整场，也不支付整个曲面的其他点对。

## 3. 实际执行顺序

1. 稀疏读取两个 README、request 和两份数学源码。只读核两 README 的当前 blob：根 74c08a36f6c997d0bc1e64a7956b42276f5fa5d7、topic bff8aea253a9e6a7a4fac28d810ac454c5499fec。
2. 核 request 完整 SHA、两源 SHA，作 AST 编译而不导入。由 request 三组参数在 runner 临时目录写本次输入。
3. Python 3.12.14 执行新联合入口，原根号精度显式128位。该新入口调用冻结 R62 内核，保留旧记录。
4. 读取本次完整临时结果，先向日志输出三个案例的全部小诊断、解析预期是否匹配、输入/输出/source/request SHA；再对配方中的准确预期做工程检查。若不符，先保存完整紧凑失败读数再令此 job 失败，不把失败解释成某个实际曲面不合格。

job 10分钟、算术 step 5分钟只是此独立小执行的资源上限；不改变任何原求解预算。没有 auth/token 提供给科学步骤，permissions 只有 contents:read，没有 Git 写操作。

## 4. 结果范围及 Rule15

结果只在 stdout 与 step summary 中给：

- 真实 run、attempt、source commit、Python版本；
- 两个原单端布尔量、联合布尔量、最终 OR、原距离与全部法向弦布尔量；
- 联合多项式全部系数、phase0/pi 精确有理余量、实根数和误差预算平方；
- 完整临时结果的大小与 SHA；
- 每例和解析预期的比较，以及全部不符项。

完整临时结果和派生输入仅在 runner 临时目录；workflow 没有 upload-artifact、Release 上传、publisher 或 commit 步骤。以后只记源、参数、真实 run、输出 SHA 和紧凑结论。

本次草稿未派发，run/job/result SHA 不预填。原源码/参数配方属于 Rule15 允许保留的重生成依据。

## 5. 已完成的源级检查

request109-source-only-check.json 记录 YAML 解析、三个 shell block 的 bash -n、两个内嵌 Python block 的 AST、两件源码真实 SHA、唯一 trigger 和 contents:read。

没有在本地导入数学源或执行任一 evaluate、Sturm、根号、范数、多项式或科学用例；没有 Git mutation、API 调用或下载。
