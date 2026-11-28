# 间隙 23/25 新固定度量的第二至第四个真实位置步

**数值证据。**

续自同一新度量自身第 1 个接受态，完整 5292 后缀位置自由，保留原始 4291840 行及全部几何、Q2 与物理 H²。每步选择由 G10 上的实际全非线性代价决定；错移 G11 另行观察。

| 自身步 | 原 G10 R² | G11 metric / κ / held |
|---:|---:|---|
| 1 | 0.1825265815 | 0.282135601 / 20.34818825 / 0.6468547291 |
| 2 | 0.080736504744 | 0.2017335744 / 19.70704504 / 0.6392111071 |
| 3 | 0.076129527839 | 0.3108836499 / 22.97513901 / 0.633470551 |
| 4 | 0.07249062221 | 0.2623440644 / 16.66732275 / 0.633511006 |

G10 四次代价连续下降，独立 metric 仅在第二步达到 .2017336，第三步反升。第二至四步的独立 held 均低于 .64，第四步 κ16.6673 仍高于 1/.097。此固定目标的真实几何与后缀候选保留各自的观察结果。

## 可移植重生

在运行目录 W 中执行。S 是公开课题 scripts 的绝对路径，E 是同次物理 IVP 采样产生 ramp-33.npz 与 ramp-65.npz 的目录。先按原记录产生 G10/G11 的原材料与原 5292 第 9 态。原命令只将脚本及 master 的位置换成这三个变量。

```sh
cd "$W"
export OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 OMP_NUM_THREADS=1
python3 -u "$S/2ecf-polar-new-central-gap-suffix-solve.py" --scripts "$S" --prepare-entry "$S/2ecf-polar-new-central-gap-compose.py" --prepared polar-new-gap-092-prepared.json --normal-audit polar-G10s-sparse-jet-full-normal-audit.json --state polar-new-gap-092-fixed-step01-step01-state.json --initial-damping 0.021333333333333333 --steps 1 --prefix polar-new-gap-092-fixed-step02
python3 -u "$S/2ecf-polar-raw-ramp-suffix-observe.py" --scripts "$S" --prepare-entry "$S/2ecf-polar-new-central-gap-compose.py" --prepared polar-new-gap-092-prepared.json --observer polar-new-gap-092-independent.json --state polar-new-gap-092-fixed-step02-step01-state.json --output polar-new-gap-092-fixed-step02-G11.json
python3 -u "$S/2ecf-polar-new-central-gap-suffix-solve.py" --scripts "$S" --prepare-entry "$S/2ecf-polar-new-central-gap-compose.py" --prepared polar-new-gap-092-prepared.json --normal-audit polar-G10s-sparse-jet-full-normal-audit.json --state polar-new-gap-092-fixed-step02-step01-state.json --initial-damping 0.021333333333333333 --steps 1 --prefix polar-new-gap-092-fixed-step03
python3 -u "$S/2ecf-polar-raw-ramp-suffix-observe.py" --scripts "$S" --prepare-entry "$S/2ecf-polar-new-central-gap-compose.py" --prepared polar-new-gap-092-prepared.json --observer polar-new-gap-092-independent.json --state polar-new-gap-092-fixed-step03-step01-state.json --output polar-new-gap-092-fixed-step03-G11.json
python3 -u "$S/2ecf-polar-new-central-gap-suffix-solve.py" --scripts "$S" --prepare-entry "$S/2ecf-polar-new-central-gap-compose.py" --prepared polar-new-gap-092-prepared.json --normal-audit polar-G10s-sparse-jet-full-normal-audit.json --state polar-new-gap-092-fixed-step03-step01-state.json --initial-damping 0.021333333333333333 --steps 1 --prefix polar-new-gap-092-fixed-step04
python3 -u "$S/2ecf-polar-raw-ramp-suffix-observe.py" --scripts "$S" --prepare-entry "$S/2ecf-polar-new-central-gap-compose.py" --prepared polar-new-gap-092-prepared.json --observer polar-new-gap-092-independent.json --state polar-new-gap-092-fixed-step04-step01-state.json --output polar-new-gap-092-fixed-step04-G11.json
```

## SHA256

| 原件 | SHA256 |
|---|---|
| polar-new-gap-092-01obs-04-driver-exit.json | b320b600bab1f47f2b26095b65b5f52a6b01ef2f45cb99a73a83312a98bdd464 |
| polar-new-gap-092-fixed-step02-initial.json | 8f2824795d543d0d1db88a40af454704ca3a2717545cc20bcd0d8580f44ff68e |
| polar-new-gap-092-fixed-step02-report.json | 28c6b79467503b9780990c211699ca3629d7bd28d1dbdda60bb3aa7f83bb50cb |
| polar-new-gap-092-fixed-step02-step01-state.json | 23dcea1c2b37cf3efdefa41e6e704963a8b070cd03e1d7b6a08c5be3ecde239b |
| polar-new-gap-092-fixed-step02-G11.json | cef5d9583d7ef08324c3968f4e74e79ed55b018ba2999bb8a4f3f23fd4435c16 |
| polar-new-gap-092-fixed-step03-initial.json | 7d7c3f86b078e052aa4141fde41732b488fe532a2af23b2e945101af3b847439 |
| polar-new-gap-092-fixed-step03-report.json | 847cc9f8e39c0044eb01361c51e906fbfa72fa9d4dcfc2038fb98808746a0f28 |
| polar-new-gap-092-fixed-step03-step01-state.json | da6fb12bcaa2387fbe1ab42d22d9120d4508d4c1e8544c39cacca7f8d19e0557 |
| polar-new-gap-092-fixed-step03-G11.json | 24cc1958b63ebfff3916bef30c333775df4a100e6f7e0f7a1731f970c32e25cc |
| polar-new-gap-092-fixed-step04-initial.json | 8abacdcd5773d980f120e427a578bcb56eae0fc2dbbdebc6c3b0b5ef1aecff6b |
| polar-new-gap-092-fixed-step04-report.json | 18b944044d3d8bcb6ec80c3e634275f3ba29fa37383834571a99679240e95d0c |
| polar-new-gap-092-fixed-step04-step01-state.json | f4283df1fcc97ea0034649f2d679bd06eefb39f4ecb49eda2c4cd6367c96dfde |
| polar-new-gap-092-fixed-step04-G11.json | d9d8ca83885f7836eebcbfc9ec0d25484ea14b32611acefa2a9db988f9bf86f6 |
| polar-new-gap-092-fixed-step02-exit.json | a7afdaf8111c285fc59c0ced377cd1bc123ee77d3110bb36d44a2510bcdeee26 |
| polar-new-gap-092-fixed-step02.log | 8fc46322e82bd122425672f5f93c7feb2142c9b642443e6f5a307e12a4735188 |
| polar-new-gap-092-fixed-step02-G11-exit.json | f6f037ed89b0d9f60e098c8fb295c09fea24ce4142b31ef18395cac17396a887 |
| polar-new-gap-092-fixed-step02-G11.log | 601e0a68ef3769d974dfaf2decf39c46ef6297f4b5b46025af6fa90af0a54f8d |
| polar-new-gap-092-fixed-step03-exit.json | 863c933defb94e7da31195193d0bbbff1e508389aca682b45133f6a97431ecdc |
| polar-new-gap-092-fixed-step03.log | ff9aee720aa531163134d2dafbe4f65956599feca1a5ff3f34c6dcecf2d67c3b |
| polar-new-gap-092-fixed-step03-G11-exit.json | 63608fe3ff59455cf0f5bac517cd402e75e48109e1db9cfab56870d13deb2d7c |
| polar-new-gap-092-fixed-step03-G11.log | c22606ff65570350b065e82d30b2ba7e8e34d95a9b9c37cd50c8c5129e27315d |
| polar-new-gap-092-fixed-step04-exit.json | fef7219ee9f445ed9c74f02ecd4d1439ba6d2c634932a125e87f9ddd8e3d08a5 |
| polar-new-gap-092-fixed-step04.log | 47ff6034a60a7f1f1638b1275f9f9ebf965a48b0e661250fe36383ab55bb075c |
| polar-new-gap-092-fixed-step04-G11-exit.json | a0b537bb4e45deede75c52894793e981e00b49ed4a0cc9364fb839c941be535d |
| polar-new-gap-092-fixed-step04-G11.log | 99326326293bcadaa2a99b3fa2bfdae221916e6dc5d1fd9452bae12e7a0d7001 |
