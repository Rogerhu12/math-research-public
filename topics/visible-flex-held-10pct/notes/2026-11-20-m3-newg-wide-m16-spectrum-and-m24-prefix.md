# m3：新 g 宽窗的 M16 实际谱与 M24 合格有限前缀

维护会话：Astra-held10-1b6d88ec-20261120。

接前条 2026-11-20-m3-newg-wide-m8-actual-spectrum-and-m16-entry.md。
本条始终保持材料核心 lambda=.002、tau=1、S=.5、b=.2、目标
k=.2，采用已执行的新多段 flat profile 和原 short bridge4。
实际 M16 场的补空间谱支持转到 M24；M24 原 BVP 与原 metric 门均
已真正通过。这不是准确圆弧 lambda=1，也不是固定 g/core 的收敛证明，
更不是完整闭面或严格存在结论。

## 1. M16 的主缺陷仍在表示之外

对同一 M16 完整 physical.npz，保 exact lift、物理 s、新 profile 和
固定 mean512 规则，两个独立只读审计都实际 exit 0。512/1024 角网格
得到相同的相对 metric 节点 operator 最大值 3.5698135864015157e-6。
峰在 s=.1995180856910552、psi=theta=pi；相对矩阵 (ss,st,tt) 为

    [-3.5698135864015157e-6, 6.377250067305464e-17,
      3.3805803112407773e-7].

M16 的实际场本身仍过不了 1e-6，不只是 FFT l1 上界保守。1024 网格
三个分量的 FFT l1 为 4.272493002263892e-6、1.3451974477315464e-6、
1.4378356587303537e-6。

同场全未投影 Frenet 残差最大值 6.032670770490156e-5，原 native
投影内径向残差仅 7.189043117045232e-8，补空间残差最大值
6.0326796884365764e-5。1024 网格的 psi 笛卡尔频壳如下；不能当成
physical theta 的 Fourier 表。

| psi 频壳 | 残差向量系数有限 l1 最大值 |
|---|---:|
| 0 | 2.5088351723442483e-13 |
| 1–3 | 8.995152506845042e-8 |
| 4–49 | 5.1137300437040704e-8 |
| 50–98 | .00012900444517732803 |
| 99–196 | 4.994307011986781e-6 |
| 197–392 | 1.3947862191179172e-7 |
| 393–512 | 3.80488898714588e-9 |

主系数包括 psi=±53、±55、±54、±59、±61，位于原 M16 笛卡尔
表示之外。Rz 零模最大值 1.2216790079566664e-15，固定 mean512 与
评价网格均值差不超过 1.3322676295501878e-15；没有另放均值自由度
来吸收这批角残差。直接 C² 切向导数诊断 max|T·R_theta| 为
1.588984267314464e-5，与 1024 点 DFT 导数的最大差为
3.2630942002680142e-9。以上都是有限数值诊断。

## 2. M24 端口的原 2 GB OOM 与共享分配恢复

首次直接调用升 M helper，在 m3-work/newg-wide-lambda0p002-m24-transfer
生成 M24/N512 settings 后，原未共享 worker port exporter 实际触发
Node 2 GB heap OOM。该次没有转移场，也没有前缀 BVP。失败 transfer.json
SHA256 为 87b2404b859359f8869bb31f2df8c70df52a1c6b79ad7d66175671fccea923e4。

随后只在独立 source 副本安装已有 shared allocation 修改，仍用
原 exporter 和原 node_heap=2048。该端口副本没有另装 periodic
quadrature patch。实际成功得到 24 个 linearSlope。数值 N=512 满足
原 N>4*M*spacing；depth8、steps16、linearSteps512、auditSteps16、
shootingParts16 和物理尾参数保持原值。首 valley control 是 4.625，
不能拿旧 3.125 尾替代。

以下复现块从前条 M16 settings 直接构造相同 M24 settings，无需重演
OOM。REPO 为仓库根，WORK 为本会话 m3-work，TOPIC 为本课题目录；
新输出目录应为空。

~~~bash
export WORK TOPIC
python - <<'PY'
import json, os
from pathlib import Path
w=Path(os.environ['WORK'])
d=w/'newg-wide-m24-port'
d.mkdir()
c=json.loads((w/'newg-wide-lambda0p002-m16-transfer/tail-settings.json').read_text())
c['modes']=24
while c['quadrature']<=4*c['modes']*c['spacing']:
    c['quadrature']*=2
(d/'tail-settings.json').write_text(json.dumps(c,indent=2)+'\n')
PY
python "$TOPIC/scripts/resume_m3/install_shared_tail_engines.py" \
  --copy-from "$WORK/multistage-source-v2" \
  --source-topic "$WORK/newg-shared-port-source" \
  --manifest "$WORK/newg-wide-m24-port/shared-install.json" \
  --export-modules "$WORK/newg-wide-m24-port/shared-modules"
env -u LD_PRELOAD -u LD_LIBRARY_PATH \
  OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 \
  VISIBLE_FLEX_SPARSE_PYTHON="$(command -v python)" \
  VISIBLE_FLEX_SPARSE_LINEAR_HELPER="$TOPIC/scripts/nonlinear_tail/m3_sparse_shooting_deliverable/sparse_shooting_linear.py" \
  python "$TOPIC/scripts/resume_m3/recovered_q021/export_original_worker_port.py" \
  --source-topic "$WORK/newg-shared-port-source" \
  --config "$WORK/newg-wide-m24-port/tail-settings.json" \
  --out "$WORK/newg-wide-m24-port/linear-port.json"
~~~

实际完整 argv 保存在 scratch 的 newg-wide-m24-port/commands.json；
当时读取失败目录中已生成的同内容 settings，随后复制到新端口目录。
成功 port SHA256 为
42369d1571413fd4ecccea43ccfef233f4b97506f71e28b86ed9735c28c2d93b，
settings SHA256 为
37bc9073d2dba1d110b165b5febbb054d1dd1a8ca09ec23b86e2d76c39f08f46。
这次只解决实际分配容量问题，没有放宽数学门。

## 3. 实际 M16→M24 完整 lift 转移

仍用 R48 公式

    Y_new = embed(Y_old) + a*chi*(I_new-embed(I_old)).

补偿系数为 1，不能再乘核心 lambda=.002。保原物理 q、delta 增量、
角图和十五个 support 控制，新增八个控制初值为 0，不是只给原状态
补零。helper 源保持前条 SHA256 c1f7741ee1882bd8413a04f280df759da4165792291f5419b243b7deed2882fe。

~~~bash
env -u LD_PRELOAD -u LD_LIBRARY_PATH \
  OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 python -u \
  "$TOPIC/scripts/resume_m3/prepare_lifted_mode_restart.py" \
  --source-run "$WORK/newg-wide-lambda0p002-m16-linear/run.json" \
  --port "$WORK/newg-wide-m24-port/linear-port.json" \
  --modes 24 --angular 768 --check-angular 2048 \
  --outdir "$WORK/newg-wide-lambda0p002-m24-transfer-shared"
~~~

实际 exit 0，检查使用 102 个 s 点、2336 个角点；连续参考图六个
jet 的最大差为

    position 3.3309139213661226e-16,
    psi      3.861075170955941e-16,
    psi_psi  1.45630836527132e-15,
    s        3.7866275808379905e-16,
    s_psi    1.3357550994815994e-15,
    s_s      5.461575137144001e-15,
    rho      0.

输出只保存节点初猜，没有声称新 BVP cubic 与原 quintic 逐点恒等。
initial.npz SHA256 为
9739f2c376fb40a382af3dac6ef6e9370214c4c52a6cafeef6583893a7935bef；
transfer.json SHA256 为
ad11ee15353d662b8154d7e5a523961c0adfc795d1314f79aeee8a280b25aa50。

## 4. M24 原求解与原 metric 门真正通过

~~~bash
env -u LD_PRELOAD -u LD_LIBRARY_PATH \
  OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 python -u \
  "$TOPIC/scripts/resume_m3/portable_prefix_continue.py" \
  --source-topic "$WORK/multistage-source-v2" \
  --short-bridge "$WORK/runtime-source/bundle/topics/visible-flex-larger-amplitude/computations/root_short_bridge.py" \
  --profile "$WORK/multistage-linear-root-profile.json" \
  --chart "$WORK/bootstrap/reference/chart.json" \
  --port "$WORK/newg-wide-m24-port/linear-port.json" \
  --raw-restart "$WORK/newg-wide-lambda0p002-m24-transfer-shared/initial.npz" \
  --core-module "$TOPIC/scripts/resume_m3/material_support_factory.py" \
  --core-config "$TOPIC/scripts/resume_m3/multistage_wide_circle_lambda0p002.json" \
  --amplitude .06 --warp-reference .06 --modes 24 --angular 768 \
  --audit-angular 512 --nodes 401 --max-nodes 6000 \
  --tol 1e-6 --bc-tol 1e-7 --physical-bc-tol 2e-9 \
  --outdir "$WORK/newg-wide-lambda0p002-m24-linear" \
  > "$WORK/newg-wide-lambda0p002-m24-linear.log" 2>&1
~~~

实际 exit 0，2 个网格、631 点，120.672 秒；DomainNewton 共 3 个完整
alpha=1 接受步，0 domain/merit 拒绝、0 no_step。

| 指标 | 实际值 |
|---|---:|
| collocation RMS max | 9.927150339177653e-7 |
| 原 metric_l1 | **6.482415924575457e-7** |
| 原 24 条 linear DN physical BC max | 3.717677792201249e-16 |
| flow_defect | 9.3585759997069e-6 |
| Darboux l1 | .004027328487102274 |
| delta | .06413464104697915 |
| raw p0 | -9.684017201077914e-6 |
| beta | .7287692832696029 |
| 原审计实际角数 | 1168 |
| 原审计 s 点数 | 1410 |

原 metric_l1<=1e-6 的有限前缀门已付；单列的 flow_defect 与 Darboux
数值不因此变成严格零，也没有宣称它们通过更强门。delta 和全部
support 控制仍是设计未知量，M8→M16→M24 的下降不是固定同一
g/core 的收敛率。

实际 c6,...,c72 为

    [.0005030007167614584, -.000040760067196837114,
     -.0000017005352258893914, .000000569000417969631,
      .0000011256106082400947, -.00000015566456401429725,
     -.0000003719745299150345, .0000001714756427406424,
      .00000011556347473447741, -.0000001182390562607273,
     -.000000018720177018564125, .00000006672720191479936,
     -.000000013020619056851519, -.00000003071711724228511,
      .00000001663657990869754, .000000012548301114124361,
     -.00000001582147986342266, .000000021587910180716612,
     -.00000004980986497546006, .0000001779919245428001,
      .00000004631112561989233, -.00000002622377499078343,
     -.000000011383729233269632].

M8 七控制严格核心盒不能自动外推到这些高模，本条没有这样使用。

| 实际对象 | SHA256 |
|---|---|
| M24 raw inner-00.npz | 1bb631d68796af48821e71baeb696a9ffa7f66f92d7cdcb3af84e27ebe08076e |
| M24 physical.npz | f2e22fe19bb0b6fdeff79c4fa99363d9be6cbb1ef382fd882679a2b717a3030d |
| M24 run.json | c44b6fd2fbb13cc9ce0451cc6ab1d3c06521de0622de27190bde94c4c550462a |

## 5. 固定 mean512 的独立实际算子检查

同一 M24 非均值场配固定 mean512 的完整 proxy 图，其 512/1024 角扫描均得到

    sampled relative operator max = 5.450092284256973e-7.

峰在 s=.13976236085430432、psi=6.19728238305799、
theta=6.224630616980418，矩阵三个分量为

    [-5.446206085002459e-7, -1.450341826367621e-8,
     -3.7370816441395505e-9].

1024 网格的三个 FFT l1 为 6.48241590851595e-7、2.1831101195848e-7、
3.672697097978012e-7；有限三角插值的行和上界为
7.830222990233957e-7。共同节点分量差全为 0。固定 mean512 后只改变
评价网格，没有增 N 时悄悄改变均值所定义的物理图。

原 prefix_audit 的完整图用 mean1168 与 GL6 height，而 physical.npz
只存非均值 quintic 和参数；本节 mean512 proxy 与原图尚无连续差量
证书。第4节原有限门由原1168规则支付，不能用本节替代。几何认证
直接绑定原1168定义；最终冻结合同须同时固定完整均值原函数规则。

有限三角插值上界还不是实际函数的全角证书；真实均值、真实积分
reference g、未采角尾和径向区间余项仍待付。也没有全 Cartesian
两阶 seam、闭合、标记破刚体、整像 held 或 reach 证明。

## 6. 审计命令及短记录

M16 独立 metric 命令与下方 M24 命令相同，只将 FIELD 和输出名中的
m24 换成 m16。全 Frenet 命令如下；审计源保持前条相同 hash。

~~~bash
FIELD="$WORK/newg-wide-lambda0p002-m16-linear"
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 python -u \
  "$TOPIC/scripts/resume_n4/audit_full_frenet_residual.py" \
  --model-adapter "$TOPIC/scripts/resume_m3/actual_m3_metric_model.py" \
  --model-config "$FIELD/run.json" --physical "$FIELD/physical.npz" \
  --metric-loader "$TOPIC/scripts/resume_m3/audit_full_relative_metric.py" \
  --mean-nodes 512 --angular 512 1024 --physical-cutoff 144 --batch 8 \
  --out "$WORK/newg-wide-lambda0p002-m16-full-residual.json"
FIELD="$WORK/newg-wide-lambda0p002-m24-linear"
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 python -u \
  "$TOPIC/scripts/resume_m3/audit_full_relative_metric.py" \
  --model-adapter "$TOPIC/scripts/resume_m3/actual_m3_metric_model.py" \
  --model-config "$FIELD/run.json" --physical "$FIELD/physical.npz" \
  --mean-nodes 512 --angular 512 1024 \
  --out "$WORK/newg-wide-lambda0p002-m24-metric-audit.json"
~~~

| 实际审计记录 | SHA256 |
|---|---|
| M16 relative metric | 779ead891f23c085343d744ed81b4117f765b0332e080b28cb07b70d172a8e05 |
| M16 full Frenet | 803c7358ecd8d70ed6b0d9bc54fdef141af960458cf08a53940f12bebb587c06 |
| M24 relative metric | 1f99c1b352a2dc0562d246c243f4c9823de23b346094fcce99a285d11a83f803 |

本条新增验收是原 **linear DN 的合格有限前缀**；真非线性尾部另行
执行和验收。可再生场、矩阵和完整运行 JSON 留 scratch，本条保存
方法、参数、完整命令、短结果与来源 hash。

